from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic import TemplateView, ListView

from .models import Car, Category


# from .serializer import CarSerializer, CategorySerializer, OrderSerializer, ClientSerializer


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["category_list"] = Category.objects.all()
		return context


class CarDetailView(DetailView):
	model = Car
	context_object_name = "car"
	template_name = "car_detail.html"




class CartView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            client = request.user
            order = Order.objects.filter(client=client).first()
            context = {'order': order}
            return render(request, 'cart.html', context)
        else:
            return redirect('login')


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, slug):
        client = request.user.client  # Assuming the user is logged in and has a Client instance
        car = get_object_or_404(Car, slug=slug)
        quantity = int(request.POST['quantity'])

        order, created = Order.objects.get_or_create(client=client, order_status=OrderStatus.PROCESSING)
        order_item, _ = OrderItem.objects.get_or_create(order=order, car=car)
        order_item.quantity += quantity
        order_item.save()

        return redirect('cart')

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, slug):
        client = request.user.client  # Assuming the user is logged in and has a Client instance
        car = get_object_or_404(Car, slug=slug)

        order = Order.objects.filter(client=client).first()
        if order:
            order_item = OrderItem.objects.filter(order=order, car=car).first()
            if order_item:
                order_item.delete()

        return redirect('cart')


class SearchResultsListView(ListView):
	model = Car
	context_object_name = "cars_list"
	template_name = "search_results.html"

	def get_queryset(self):
		query = self.request.GET.get("q")
		return Car.objects.filter(Q(model__icontains=query))


# class CarViewSet(viewsets.ModelViewSet):
# 	queryset = Car.objects.all()
# 	serializer_class = CarSerializer
#
#
# class OrderViewSet(viewsets.ModelViewSet):
# 	queryset = Order.objects.all()
# 	serializer_class = OrderSerializer
#
# 	def perform_create(self, serializer):
# 		# Saves the order using the serializer.
# 		order = serializer.save()
# 		# Iterates through all cars related to the order.
# 		for order_item in order.order_items.all():
# 			car = order_item.car
# 			car.quantity -= order_item.quantity
# 			car.save()
# 			update_car_quantity_in_warehouse.delay(car.id, car.quantity)
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
# 	queryset = Category.objects.all()
# 	serializer_class = CategorySerializer
#
#
# class ClientViewSet(viewsets.ModelViewSet):
# 	queryset = Client.objects.all()
# 	serializer_class = ClientSerializer


class AboutPageView(TemplateView):
	template_name = "about.html"


class CarListView(ListView):
	model = Car
	context_object_name = "car_list"
	template_name = "cars_list.html"


class CategoryListView(ListView):
	model = Category
	context_object_name = "category_list"
	template_name = "category_list.html"




#
# def get_client(request):
# 	try:
# 		client = Client.objects.get(user=request.user)
# 	except Client.DoesNotExist:
# 		# Handle the case when the client does not exist.
# 		client = None
# 	return client
#
#
# def add_car_to_cart(request, slug):
# 	client = get_client(request)
# 	car = get_object_or_404(Car, slug=slug)
# 	cart, _ = Order.objects.get_or_create(client=client)
#
# 	cart_item, created = OrderItem.objects.get_or_create(cart=cart, car=car)
# 	if not created:
# 		cart_item.quantity += 1
# 		cart_item.save()
#
# 	return redirect('cart_view')
#
#
# def cart_view(request):
# 	client = get_client(request)
# 	cart, _ = Order.objects.get_or_create(client=client)
# 	cart_items = Order.objects.filter(cart=cart)
#
# 	context = {
# 		'cart_items': cart_items,
# 	}
# 	return render(request, 'cart.html', context)

