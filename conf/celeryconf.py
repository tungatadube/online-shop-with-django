import os
import logging

from django.conf import settings
from celery import Celery

settings_module = settings.__module__

logger = logging.getLogger(__name__)
logger.info(f'Setting the default Django_SETTINGS_MODULE as {settings_module} for the celery program')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()