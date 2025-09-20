from django.contrib.auth import get_user_model
from django.db import models

from common.constants.method import HttpMethods
from common.models.base import TimestampMixin, UUIDMixin

User = get_user_model()


class LogRequest(UUIDMixin, TimestampMixin):
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True,  verbose_name='Người dùng')
    path = models.CharField('URL', max_length=256)
    method = models.CharField('Phương thức', max_length=16, choices=HttpMethods.choices())
    ip_address = models.GenericIPAddressField('Địa chỉ IP', null=True, blank=True)
    user_agent = models.TextField('User Agent', null=True, blank=True)
    status_code = models.PositiveSmallIntegerField('Mã')
    response_time_ms = models.PositiveIntegerField('Thời gian (ms)')

    class Meta:
        db_table = 'log_requests'
        verbose_name = 'Nhật ký yêu cầu'
        verbose_name_plural = 'Nhật ký yêu cầu'
