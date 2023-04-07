from DRF_CarDealer.apps.users.models import Client
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = Client
		fields = ["first_name", "last_name", "email"]


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = Client
		fields = ["first_name", "last_name",]
