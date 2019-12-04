# Create your views here.
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cart.forms import CartAddProductForm
from shop.models import Category, Product
from shop.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, category_slug=None, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(available=True))
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def product_detail(request, pk, ):
    product = get_object_or_404(Product, id=pk, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/product/detail.html", {"product": product, 'cart_product_form': cart_product_form})


def product_list(request, category_slug=None, ):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, "shop/product/list.html", {"products": products,
                                                      "category": category,
                                                      "categories": categories})
