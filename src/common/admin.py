from django.contrib import admin

from .models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'location', 'message_short', 'exception_type', 'created_at')
    list_filter = ('level',)
    search_fields = ('message', 'location')

    def message_short(self, obj):
        return obj.message[:32]
    message_short.short_description = 'Message'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
