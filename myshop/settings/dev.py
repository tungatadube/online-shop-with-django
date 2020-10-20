from braintree import Configuration, Environment
from django.core.mail import send_mail

import myshop.config.parameters as secret
from .base import *

MEDIA_URL = BASE_DIR + "/media/"
MEDIA_ROOT = MEDIA_URL
STATIC_URL = BASE_DIR + '/static/'
STATIC_ROOT = STATIC_URL

# messaging settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = secret.username
EMAIL_HOST_PASSWORD = secret.password
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

list_of_emails = ['physicshlf@gmail.com']
checks = False

if checks:
    def send():
        return send_mail('Django mail', 'This message was sent with Django.',
                         'tungatadube@gmail.com',
                         list_of_emails, fail_silently=False)


    try:

        send()
        logger.info(f"Email from {secret.username} to {list_of_emails} was successful")
    except Exception as e:
        logger.info(f"{e}")

# Braintree
BRAINTREE_MERCHANT_ID = secret.BRAINTREE_MERCHANT_ID
BRAINTREE_PUBLIC_KEY = secret.BRAINTREE_PUBLIC_KEY
BRAINTREE_PRIVATE_KEY = secret.BRAINTREE_PRIVATE_KEY

Configuration.configure(
    Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)
