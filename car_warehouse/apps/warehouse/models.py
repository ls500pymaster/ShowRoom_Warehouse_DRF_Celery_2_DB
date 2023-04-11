import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("suv", "SUV"),
        ('sedan', 'Sedan'),
        ('hybrid', 'Hybrid'),
        ("electric", "Electric"),
        ('performance', 'Performance'),
        ('future', 'Future'),
    ]
    name = models.CharField(max_length=15, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    engine = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    warehouse_count = models.PositiveIntegerField(default=0)


class Client(AbstractUser):
	GENDER_CHOICES = [
		("M", "Male"),
		("F", "Female"),
		("O", "Other"),
	]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)
	email = models.EmailField()
	age = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	info = models.CharField(max_length=256, blank=True, null=True)

	def get_full_name(self):
		"""
		:return: The first_name + last_name with space between
		"""
		full_name = "%s %s" % (self.first_name, self.last_name)

	def __str__(self):
		return f"{self.first_name}"
