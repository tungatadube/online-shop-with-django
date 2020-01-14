import logging

from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem
from orders.tasks import order_created

logger = logging.getLogger(__name__)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # clear the cart
            logger.info("Clearing cart after successful post")
            cart.clear()
            logger.info(f"Launching asynchronous email task for order {order.id}")
            order_created.delay(order.id)
            # set order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
