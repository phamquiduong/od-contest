from django.contrib import admin

from mail.models.log_email import LogEmail


@admin.register(LogEmail)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'to', 'template_name', 'status', 'created_at', 'sent_at')
    list_filter = ('template_name', 'status')
    search_fields = ('to', 'template_name')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
