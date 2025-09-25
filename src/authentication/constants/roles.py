from common.models.base import DjangoChoicesEnum


class Roles(str, DjangoChoicesEnum):
    ADMIN = 'Quản trị'
