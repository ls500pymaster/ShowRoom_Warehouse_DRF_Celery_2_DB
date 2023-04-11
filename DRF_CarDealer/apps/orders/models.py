import uuid
from django.conf import settings
from django.db import models
from DRF_CarDealer.apps.users.models import Client
from DRF_CarDealer.apps.cars.models import Car


class CartItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cart_items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# class OrderStatus(models.TextChoices):
#     PENDING = "pending", "Pending"
#     PROCESSING = "processing", "Processing"
#     READY = "ready", "Ready"
#     COMPLETED = "completed", "Completed"
#     CANCELED = "canceled", "Canceled"
#
#
# class Order(models.Model):
#     client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="cart")
#     cars = models.ManyToManyField(Car, through='OrderCar')  # added many-to-many relationship with Car through OrderCar
#     quantity = models.PositiveIntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     order_status = models.CharField(choices=OrderStatus.choices, max_length=20, default=OrderStatus.PROCESSING)
#
#     def __str__(self):
#         return f"Order {self.id} by {self.client.first_name}"
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#
#     def sum(self):
#         return self.car.price * self.quantity
#
#     def __str__(self):
#         return f"Order item: {self.car} x {self.quantity} in order {self.order.id}"

