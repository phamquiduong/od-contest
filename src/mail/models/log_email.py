from django.db import models

from common.models.base import TimestampMixin, UUIDMixin
from mail.constants.email import EmailStatus
from mail.constants.template import EmailTemplates


class LogEmail(UUIDMixin, TimestampMixin):
    to = models.EmailField('Gửi đến')
    cc = models.CharField(max_length=256, null=True, blank=True)
    bcc = models.CharField(max_length=256, null=True, blank=True)

    subject = models.CharField('Chủ đề', max_length=256)
    template_name = models.CharField('Tên mẫu', max_length=128, choices=EmailTemplates.choices())
    context = models.JSONField('Tham số', blank=True, null=True)

    status = models.CharField('Trạng thái', max_length=16,
                              choices=EmailStatus.choices(), default=EmailStatus.PENDING)
    error_message = models.TextField('Lỗi', blank=True, null=True)
    sent_at = models.DateTimeField('Thời gian gửi', blank=True, null=True)

    def send(self):
        from celery_tasks.tasks.send_mail import send_email_task  # pylint: disable=C0415
        send_email_task.delay(self.id)

    class Meta:
        db_table = 'log_emails'
        verbose_name = 'Nhật ký gửi mail'
        verbose_name_plural = 'Nhật ký gửi mail'
