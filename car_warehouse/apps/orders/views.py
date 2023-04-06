from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		orders = [{"id": order.id, "model": order.order_id_store, "warehouse count": order.quantity} for order in
		                  queryset]
		return Response(orders)


class OrderItemViewSet(viewsets.ModelViewSet):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemSerializer
