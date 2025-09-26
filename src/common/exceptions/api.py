from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError) and isinstance(response.data, dict):
            fields = []
            for field, messages in response.data.items():
                error_items = [
                    {
                        'message': str(msg),
                        'code': getattr(msg, 'code', 'invalid')
                    }
                    for msg in messages
                ]
                fields.append({'name': field, 'errors': error_items})

            response.data = {
                'success': False,
                'message': 'Validation failed',
                'fields': fields
            }
        else:
            response.data = {
                'success': False,
                'message': response.data.get('detail', str(exc)) if response.data else 'Unknown',
                'fields': []
            }
        return response

    return Response({
        'success': False,
        'message': 'Internal server error',
        'fields': []
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
