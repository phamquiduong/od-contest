from typing import Any

from celery import shared_task
from celery.app.task import Task

from mail.schemas import EmailMeta
from mail.services import EmailService


@shared_task(bind=True)
def send_email_task(
    self: Task,
    to: list[str],
    meta_dict: dict,
    context: dict[str, Any] | None = None
):
    meta = EmailMeta(**meta_dict)
    email_service = EmailService(meta=meta, context=context)

    try:
        email_service.send_email(to=to)
        return f'Sent email [{meta.template_name}] to [{', '.join(to)}]'
    except Exception as exc:
        raise self.retry(exc=exc)
