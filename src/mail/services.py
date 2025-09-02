from typing import Any

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from mail.schemas import EmailMeta


class EmailService:
    def __init__(self, meta: EmailMeta, context: dict[str, Any] | None = None) -> None:
        self._meta = meta
        self._context = context

    def _build_body(self) -> str:
        return render_to_string(f'email/{self._meta.template_name}.html', self._context)

    def send_email(self, to: list[str]) -> None:
        html_content = self._build_body()

        msg = EmailMultiAlternatives(
            subject=self._meta.subject,
            body=html_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to, bcc=self._meta.bcc, cc=self._meta.cc
        )

        print(f'Subject: {msg.subject} | From: {msg.from_email} | To: {msg.to} | CC: {msg.cc} | BCC: {msg.bcc}')

        msg.attach_alternative(html_content, "text/html")
        msg.send()
