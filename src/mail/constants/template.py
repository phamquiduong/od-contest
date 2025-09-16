from common.models.base import DjangoChoicesEnum


class EmailTemplates(DjangoChoicesEnum):
    TEST = 'test_email'
