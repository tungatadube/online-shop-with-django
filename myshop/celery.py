import logging
import os

from celery import Celery
from django.conf import settings

settings_module = settings.SETTINGS_MODULE
logger = logging.getLogger(__name__)
logger.info('Exporting DJANGO_SETTINGS_MODULE to the system')
os.system(f'export DJANGO_SETTINGS_MODULE={settings_module}')
logger.info(f'Setting the default Django_SETTINGS_MODULE as {settings_module} for the celery program')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
