
from web.models.base import DjangoChoicesEnum


class EmailStatus(DjangoChoicesEnum):
    PENDING = 'Đợi'
    SENT = 'Đã gửi'
    FAILED = 'Lỗi'
