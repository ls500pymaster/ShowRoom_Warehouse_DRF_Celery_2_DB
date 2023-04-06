from django.contrib import admin
from .models import Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	list_filter = ("age", "gender")
	search_fields = ("email", "last_name")
	