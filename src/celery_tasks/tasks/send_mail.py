from celery import shared_task
from celery.app.task import Task
from django.conf import settings
from django.utils import timezone

from mail.constants.email import EmailStatus
from mail.models.email_log import EmailLog
from mail.services import EmailService


@shared_task(bind=True, queue=settings.CELERY_EMAIL_QUEUE)
def send_email_task(self: Task, email_log_id: str):
    email_log = EmailLog.objects.get(id=email_log_id)

    email_service = EmailService.from_template(
        subject=email_log.subject,
        template_name=email_log.template_name,
        context=email_log.context
    )

    try:
        email_service.send_email(
            to=email_log.to,
            bcc=(email_log.bcc or '').split(','),
            cc=(email_log.cc or '').split(',')
        )

        email_log.status = EmailStatus.SENT.value
        email_log.sent_at = timezone.now()

        return f'Sent email [{email_log.template_name}] to {email_log.to}'
    except Exception as exc:
        email_log.status = EmailStatus.FAILED.value
        email_log.error_message = str(exc)

        raise exc
    finally:
        email_log.save()
