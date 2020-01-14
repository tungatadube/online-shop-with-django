from django.db import models
from django.urls import reverse

from shop.helper.timestamphelper import TimestampedModel


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, )
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.slug, ])

    def __str__(self):
        return self.name


class Product(TimestampedModel):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, )
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="produts/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,])

    def __str__(self):
        return self.name
