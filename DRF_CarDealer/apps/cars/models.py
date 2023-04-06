import uuid

from django.db import models
from django.utils.text import slugify

from DRF_CarDealer.apps.users.models import Client
from DRF_CarDealer.core.models import BaseImage


class Category(models.Model):
	CATEGORY_CHOICES = [
		("suv", "SUV"),
		('sedan', 'Sedan'),
		('hybrid', 'Hybrid'),
		("electric", "Electric"),
		('performance', 'Performance'),
		('future', 'Future'),
	]
	name = models.CharField(max_length=15, choices=CATEGORY_CHOICES , unique=True)
	slug = models.SlugField(max_length=15, unique=True, blank=True)

	def __str__(self):
		return self.slug

	def save(self, *args, **kwargs):
		if not self.slug or self.name_changed():
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def name_changed(self):
		original = Category.objects.filter(pk=self.pk).first()
		return original and original.name != self.name


class CategoryImage(BaseImage):
	category = models.OneToOneField(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="category_image")


class Car(models.Model):
	FUEL_CHOICES = [
		("gasoline", "Gasoline"),
		("diesel", "Diesel"),
		("hybrid", "Hybrid"),
		("electricity", "Electricity"),
	]

	DRIVE_WHEEL_CHOICES = [
		("awd", "AWD"),
		("rwd", "RWD"),
		("fwd", "FWD"),
	]

	manufacturer = models.CharField(max_length=6, default="Lexus")
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	model = models.CharField(max_length=7)
	color = models.CharField(max_length=50, null=True, blank=True)
	engine = models.CharField(max_length=10, null=True, blank=True)
	engine_displacement = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	fuel_type = models.CharField(max_length=15, choices=FUEL_CHOICES, null=True, blank=True)
	horsepower = models.PositiveIntegerField(null=True, blank=True)
	torque = models.PositiveIntegerField(null=True, blank=True)
	transmission = models.CharField(max_length=50, null=True, blank=True)
	drive_wheels = models.CharField(max_length=3, choices=DRIVE_WHEEL_CHOICES, null=True, blank=True)
	acceleration = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
	slug = models.SlugField(max_length=30, blank=True, unique=True)

	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	warehouse_count = models.PositiveIntegerField(default=0)

	def save(self, *args, **kwargs):
		if not self.slug or self.name_changed():
			self.slug = slugify(f"{self.model} {self.drive_wheels}")
		super(Car, self).save(*args, **kwargs)

	def name_changed(self):
		if self.pk is None:
			return True
		original = Car.objects.get(pk=self.pk)
		if original is None:
			return True
		return original.model != self.model or original.drive_wheels != self.drive_wheels

	def __str__(self):
		return self.slug


class CarImage(BaseImage):
	car = models.ImageField(Car, upload_to="car_images", default="lexus.jpg")


class OrderStatus(models.TextChoices):
	PENDING = "pending", "Pending"
	PROCESSING = "processing", "Processing"
	READY = "ready", "Ready"
	COMPLETED = "completed", "Completed"
	CANCELED = "canceled", "Canceled"


class Order(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="cart")
	car = models.ManyToManyField(Car, related_name='cars')
	quantity = models.PositiveIntegerField()
	order_date = models.DateTimeField(auto_now_add=True)
	order_status = models.CharField(choices=OrderStatus.choices, max_length=20, default=OrderStatus.PROCESSING)

	def __str__(self):
		return f"Order {self.id} by {self.client.first_name}"


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()

	def sum(self):
		return self.car.price * self.quantity

	def __str__(self):
		return f"Order item: {self.car} x {self.quantity} in order {self.order.id}"
