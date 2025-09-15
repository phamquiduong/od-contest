from common.models.base import DjangoChoicesEnum


class LogLevel(DjangoChoicesEnum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'
