import logging

from celery import task

from django.core.mail import send_mail
from .models import Order
from myshop.config.parameters import username

logger = logging.getLogger(__name__)
@task
def order_created(order_id):
    """
    Task to send admin email when an order has been received
    :param order_id:
    :return: int
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order {order.id}"
    message = f"Dear {order.first_name} \n\nYou have successfully placed an order. Your order id is {order.id}"
    logger.info(f"Sending email for order {order.id}")
    return send_mail(subject, message, username, [order.email])
