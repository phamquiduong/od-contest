import uuid

from django.contrib.auth import get_user_model
from django.db import models

from common.models.base import TimestampMixin
from upload.constants.visibility import Visibilities

User = get_user_model()


def upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'original/{uuid.uuid4().hex}.{ext}'
    return filename


class FileManager(TimestampMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    original_name = models.CharField(max_length=256)
    file = models.FileField(upload_to=upload_path)
    visibility = models.CharField(max_length=16, choices=Visibilities.choices(), default=Visibilities.PRIVATE)

    class Meta:
        db_table = 'files_manager'
        verbose_name = 'Quản lý file'
        verbose_name_plural = 'Quản lý file'
