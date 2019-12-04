
from django.urls import path

from cart.views import cart_add, cart_detail, cart_remove

urlpatterns = [
    path("api/v1/", cart_detail, name="cart_detail"),
    path("api/v1/add/<int:product_id>/", cart_add, name="cart_add"),
    path("api/v1/remove/<int:product_id>/", cart_remove, name="cart_remove"),

]




