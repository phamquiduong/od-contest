from common.models.base import DjangoChoicesEnum


class Visibilities(str, DjangoChoicesEnum):
    PUBLIC = 'Công khai'
    PRIVATE = 'Chỉ mình tôi'
