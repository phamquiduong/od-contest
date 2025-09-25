
from common.models.base import DjangoChoicesEnum


class EmailStatus(str, DjangoChoicesEnum):
    PENDING = 'Đợi'
    SENT = 'Đã gửi'
    FAILED = 'Lỗi'
