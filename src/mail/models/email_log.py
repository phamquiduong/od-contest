from django.db import models

from mail.constants.email import EmailStatus
from web.models.base import TimestampMixin, UUIDMixin


class EmailLog(UUIDMixin, TimestampMixin):
    to = models.EmailField()
    cc = models.CharField(max_length=255, null=True, blank=True)
    bcc = models.CharField(max_length=255, null=True, blank=True)

    subject = models.CharField(max_length=255)
    template_name = models.CharField(max_length=128)
    context = models.JSONField(blank=True, null=True)

    status = models.CharField(max_length=16, choices=EmailStatus.choices(), default=EmailStatus.PENDING.value)
    error_message = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'email_logs'
        ordering = ['-updated_at']
