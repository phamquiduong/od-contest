from django.db import models

from common.models.base import TimestampMixin, UUIDMixin
from mail.constants.email import EmailStatus


class LogEmail(UUIDMixin, TimestampMixin):
    to = models.EmailField('Gửi đến')
    cc = models.CharField(max_length=256, null=True, blank=True)
    bcc = models.CharField(max_length=256, null=True, blank=True)

    subject = models.CharField('Chủ đề', max_length=256)
    template_name = models.CharField('Tên mẫu', max_length=128)
    context = models.JSONField('Tham số', blank=True, null=True)

    status = models.CharField('Trạng thái', max_length=16, choices=EmailStatus.choices(),
                              default=EmailStatus.PENDING.value)
    error_message = models.TextField('Lỗi', blank=True, null=True)
    sent_at = models.DateTimeField('Được gửi lúc', blank=True, null=True)

    class Meta:
        db_table = 'log_emails'
        ordering = ['-updated_at']
