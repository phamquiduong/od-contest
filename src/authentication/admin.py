from django.contrib import admin

from authentication.models import User


@admin.register(User)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')
    list_filter = ('role',)
    ordering = ('-updated_at',)
