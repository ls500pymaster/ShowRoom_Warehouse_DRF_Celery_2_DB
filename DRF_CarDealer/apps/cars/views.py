from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from .models import Car, Client, Order, OrderItem
from .models import Category
from .serializer import CarSerializer, CategorySerializer, OrderSerializer, ClientSerializer

from DRF_CarDealer.apps.cars.tasks import update_car_quantity_in_warehouse


def index(request):
	cars = Car.objects.all()
	context = {"cars": cars}
	return render(request, "index.html", context)


def get_client(request):
	try:
		client = Client.objects.get(user=request.user)
	except Client.DoesNotExist:
		# Handle the case when the client does not exist.
		client = None
	return client


def add_car_to_cart(request, slug):
	client = get_client(request)
	car = get_object_or_404(Car, slug=slug)
	cart, _ = Order.objects.get_or_create(client=client)

	cart_item, created = OrderItem.objects.get_or_create(cart=cart, car=car)
	if not created:
		cart_item.quantity += 1
		cart_item.save()

	return redirect('cart_view')


def cart_view(request):
	client = get_client(request)
	cart, _ = Order.objects.get_or_create(client=client)
	cart_items = Order.objects.filter(cart=cart)

	context = {
		'cart_items': cart_items,
	}
	return render(request, 'cart.html', context)


class CarViewSet(viewsets.ModelViewSet):
	queryset = Car.objects.all()
	serializer_class = CarSerializer


class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def perform_create(self, serializer):
		# Saves the order using the serializer.
		order = serializer.save()
		# Iterates through all cars related to the order.
		for order_item in order.order_items.all():
			car = order_item.car
			car.quantity -= order_item.quantity
			car.save()
			update_car_quantity_in_warehouse.delay(car.id, car.quantity)


class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

