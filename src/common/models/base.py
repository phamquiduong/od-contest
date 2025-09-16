import uuid
from enum import Enum

from django.db import models


class DjangoChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(member.value, member.name) for member in cls]

    @classmethod
    def values(cls):
        return [member.value for member in cls]

    @classmethod
    def names(cls):
        return [member.name for member in cls]


class TimestampMixin(models.Model):
    created_at = models.DateTimeField('Thời gian tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Thời gian cập nhật', auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    # Will update to UUID7 in the feature
    id = models.UUIDField('Mã UUID', primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AdminLogPermissionMixin:
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
