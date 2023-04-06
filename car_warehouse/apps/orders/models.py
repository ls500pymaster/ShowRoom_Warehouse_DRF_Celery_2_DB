import uuid

from django.db import models


class OrderStatus(models.TextChoices):
	PENDING = "pending", "Pending"
	PROCESSING = "processing", "Processing"
	READY = "ready", "Ready"
	COMPLETED = "completed", "Completed"
	CANCELED = "canceled", "Canceled"


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	client_email = models.EmailField(null=True, blank=True)
	order_status = models.CharField(choices=OrderStatus.choices, max_length=20, default=OrderStatus.PROCESSING)
	quantity = models.PositiveIntegerField()
	order_date = models.DateTimeField(auto_now_add=True)
	order_id_store = models.CharField(max_length=100, null=True, blank=True)


class OrderItem(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="warehouse_order_items")
	model = models.CharField(max_length=50)
	quantity = models.PositiveIntegerField()

	def __str__(self):
		return f"Order item: {self.model} x {self.quantity} in order {self.order_id.id}"
