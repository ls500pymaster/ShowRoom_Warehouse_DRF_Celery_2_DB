import uuid
from django.conf import settings
from django.db import models
from DRF_CarDealer.apps.users.models import Client
from DRF_CarDealer.apps.cars.models import Car
from decimal import Decimal
from django.conf import settings

class CartItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.IntegerField(default=1, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cart_items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
