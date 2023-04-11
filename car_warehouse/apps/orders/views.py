from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(generics.CreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		orders = [{"id": order.id, "model": order.order_id_store, "warehouse count": order.quantity} for order in
		                  queryset]
		return Response(orders)
