from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
	list_display = ("client", "quantity", "order_status")


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
	list_display = ("order", "car", "quantity")
