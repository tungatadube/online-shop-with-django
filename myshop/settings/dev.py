from django.core.mail import send_mail

from conf.parameters import username, password
from .base import *

MEDIA_URL = BASE_DIR + "/media/"
MEDIA_ROOT = MEDIA_URL
STATIC_URL = BASE_DIR + '/static/'
STATIC_ROOT = STATIC_URL

# messaging settings

EMAIL_HOST = "smtp.outlook.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = username
EMAIL_HOST_PASSWORD = password
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

list_of_emails = ['mduduzi.frederick.dube@outlook.com']


def send():
    return send_mail('Django mail', 'This message was sent with Django.',
                     'tungatadube@gmail.com',
                     list_of_emails, fail_silently=False)


try:
    send()
    logger.info(f"Email from {username} to {list_of_emails} was successful")
except Exception as e:
    logger.info(f"{e}")
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    send()
