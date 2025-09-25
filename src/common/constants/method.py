from common.models.base import DjangoChoicesEnum


class HttpMethods(str, DjangoChoicesEnum):
    GET = 'GET'
    POST = 'POST'
