from django.db import models

from DRF_CarDealer.apps.cars.models import Car
from DRF_CarDealer.apps.users.models import Client

class Cart(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s Cart"

class CartItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cart_items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.car}"

