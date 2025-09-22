from django.contrib import admin

from upload.models import FileManager


@admin.register(FileManager)
class FileManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'original_name', 'file', 'visibility',)
    list_filter = ('visibility',)
    ordering = ('-updated_at',)
