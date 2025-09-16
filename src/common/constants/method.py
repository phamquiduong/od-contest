from common.models.base import DjangoChoicesEnum


class HttpMethods(DjangoChoicesEnum):
    GET = 'GET'
    POST = 'POST'
