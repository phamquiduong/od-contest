from common.models.base import DjangoChoicesEnum


class EmailTemplates(str, DjangoChoicesEnum):
    TEST = 'test_email'
