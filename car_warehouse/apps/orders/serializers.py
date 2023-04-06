from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItem
		field = "__all__"


class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		field = "__all__"
