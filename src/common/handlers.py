import logging
import traceback

from django.utils.module_loading import import_string


class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        try:
            LogEntry = import_string('common.models.log_entry.LogEntry')  # pylint: disable=C0103

            exc_text = None
            exc_type_name = None
            if record.exc_info:
                exc_type, exc_value, tb = record.exc_info
                exc_type_name = exc_type.__name__ if exc_type else None
                exc_text = ''.join(traceback.format_exception(exc_type, exc_value, tb))

            LogEntry.objects.create(
                level=record.levelname,
                exception_type=exc_type_name,
                message=record.getMessage(),
                location=f'{record.filename}:{record.lineno}',
                exc=exc_text,
            )
        except Exception:
            logging.getLogger('django').exception('Failed to write log to DB')
