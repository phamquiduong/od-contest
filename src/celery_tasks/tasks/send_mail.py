from dataclasses import dataclass
from typing import Any

from celery import shared_task
from celery.app.task import Task
from django.conf import settings

from mail.services import EmailService


@dataclass
class SendEmailTaskArgs:
    subject: str
    template_name: str
    to: list[str] | str
    context: dict[str, Any] | None = None
    bcc: list[str] | None = None
    cc: list[str] | None = None


@shared_task(bind=True, queue=settings.CELERY_EMAIL_QUEUE)
def send_email_task(
    self: Task,
    subject: str,
    template_name: str, context: dict[str, Any] | None,
    to: list[str] | str,
    bcc: list[str] | None,
    cc: list[str] | None,
):
    email_service = EmailService.from_template(subject=subject, template_name=template_name, context=context)

    try:
        email_service.send_email(to=to, bcc=bcc, cc=cc)
        return f'Sent email [{template_name}] to {to}'
    except Exception as exc:
        raise self.retry(exc=exc)
