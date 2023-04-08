from django.contrib import admin
from .models import Client
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	list_filter = ("age", "gender")
	search_fields = ("email", "last_name")



