from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser, User
from django.db import models


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
