from dataclasses import asdict
from typing import Any
from mail.schemas import EmailMeta
from mail.tasks.send_mail import send_email_task


def send_email_by_celery(
    to: list[str],
    meta: EmailMeta,
    context: dict[str, Any] | None = None
):
    send_email_task.delay(  # type: ignore
        to=to,
        meta_dict=asdict(meta),
        context=context,
    )
