import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery(f'{settings.PROJECT_NAME}:{settings.ENVIRONMENT}')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
