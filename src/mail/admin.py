from django.contrib import admin

from common.models.base import AdminLogPermissionMixin
from mail.models import LogEmail


@admin.register(LogEmail)
class EmailLogAdmin(AdminLogPermissionMixin, admin.ModelAdmin,):
    list_display = ('id', 'to', 'cc', 'bcc', 'subject', 'template_name', 'status', 'error_message', 'sent_at')
    list_filter = ('template_name', 'status')
    ordering = ('-updated_at',)
