import logging
import time
from http import HTTPMethod

from django.http import HttpRequest

from common.models import LogRequest

logger = logging.getLogger()


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        start_time = time.perf_counter()
        user = request.user if request.user.is_authenticated else None
        ip = self._get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        method = request.method

        response = self.get_response(request)

        duration = (time.perf_counter() - start_time) * 1000

        if method == HTTPMethod.POST:
            try:
                LogRequest.objects.create(
                    user=user,
                    path=request.path,
                    method=method,
                    ip_address=ip,
                    user_agent=user_agent,
                    status_code=response.status_code,
                    response_time_ms=int(duration),
                )
            except Exception:
                logger.exception('Request log error')

        return response

    def _get_client_ip(self, request: HttpRequest) -> str | None:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')
