import uuid

from django.db import models
from ..warehouse.models import Car, Client


class OrderStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    PROCESSING = "processing", "Processing"
    READY = "ready", "Ready"
    COMPLETED = "completed", "Completed"
    CANCELED = "canceled", "Canceled"


class Order(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="templates")
    cars = models.ManyToManyField(Car, through='OrderCar')  # added many-to-many relationship with Car through OrderCar
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=OrderStatus.choices, max_length=20, default=OrderStatus.PROCESSING)

    def __str__(self):
        return f"Order {self.id} by {self.client.first_name}"


class OrderCar(models.Model):  # added new intermediate model OrderCar
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # moved quantity field from OrderItem to OrderCar

    def __str__(self):
        return f"Order item: {self.car.model} x {self.quantity} in order {self.order.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def sum(self):
        return self.car.price * self.quantity

    def __str__(self):
        return f"Order item: {self.car} x {self.quantity} in order {self.order.id}"

