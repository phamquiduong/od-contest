from typing import Any

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailService:
    """
    Simple service to send emails in plain text or HTML mode.
    """

    def __init__(self, subject: str, body: str, html_mode: bool) -> None:
        """
        Initialize the email with subject, body, and HTML mode.
        """

        self.subject = subject
        self.body = body
        self.html_mode = html_mode

    @classmethod
    def from_template(cls, subject: str, template_name: str, context: dict[str, Any] | None = None):
        """
        Create an EmailService instance from a Django HTML template.
        """

        body = render_to_string(f'email/{template_name}.html', context)
        return cls(subject=subject, body=body, html_mode=True)

    @classmethod
    def from_html_text(cls, subject: str, html_content: str):
        """
        Create an EmailService instance from raw HTML content.
        """

        return cls(subject=subject, body=html_content, html_mode=True)

    @classmethod
    def from_plain_text(cls, subject: str, text: str):
        """
        Create an EmailService instance from plain text.
        """

        return cls(subject=subject, body=text, html_mode=False)

    def send_email(self, to: str | list[str], bcc: list[str] | None = None, cc: list[str] | None = None) -> None:
        """
        Send the email using Django's EmailMultiAlternatives.

        Args:
            to: recipient(s) email address
            bcc: optional BCC recipients
            cc: optional CC recipients
        """

        # normalize single email string to list
        to = [to] if isinstance(to, str) else to
        bcc = bcc or []
        cc = cc or []

        msg = EmailMultiAlternatives(
            subject=self.subject,
            body=self.body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to,
            bcc=bcc,
            cc=cc
        )

        if self.html_mode:
            msg.attach_alternative(self.body, 'text/html')

        msg.send()
