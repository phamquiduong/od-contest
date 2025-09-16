from django.contrib import admin

from common.models import LogRequest
from common.models.base import AdminLogPermissionMixin


@admin.register(LogRequest)
class RequestLogAdmin(AdminLogPermissionMixin, admin.ModelAdmin):
    list_display = ('id', 'user', 'path', 'method', 'ip_address', 'user_agent', 'status_code',
                    'response_time_ms', 'created_at')
    list_filter = ('method', 'status_code')
    ordering = ('-updated_at',)
