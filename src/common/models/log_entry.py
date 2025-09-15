from django.db import models

from common.constants.log import LogLevel
from common.models.base import UUIDMixin


class LogEntry(UUIDMixin):
    level = models.CharField('Mức độ', max_length=16, choices=LogLevel.choices(), db_index=True)

    message = models.TextField('Tin nhắn')

    location = models.CharField('Vị trí', max_length=256)

    exception_type = models.CharField('Loại ngoại lệ', max_length=128, null=True, blank=True)
    exc = models.TextField('Ngoại lệ', null=True, blank=True)

    created_at = models.DateTimeField('Được tạo lúc', auto_now_add=True)

    class Meta:
        db_table = 'log_entries'
        ordering = ['-created_at']
