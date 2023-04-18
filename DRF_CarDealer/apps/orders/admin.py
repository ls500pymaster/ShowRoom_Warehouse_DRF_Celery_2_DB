from django.contrib import admin

from DRF_CarDealer.apps.orders.models import CartItem


@admin.register(CartItem)
class AdminCartItem(admin.ModelAdmin):
	list_display = ("car", "quantity")
