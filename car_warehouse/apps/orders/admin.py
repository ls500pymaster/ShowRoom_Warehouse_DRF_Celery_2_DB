from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
	list_display = ("id", "order_status", "quantity")
	list_filter = ("order_status", )


@admin.register(OrderItem)
class AdminOrderItem(admin.ModelAdmin):
	list_display = ("order_id", "model", "quantity")
	list_filter = ("order_id",)
