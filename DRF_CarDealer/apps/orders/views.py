from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from rest_framework import status
from DRF_CarDealer.apps.cars.models import Car
from .models import CartItem, Order
import requests


@login_required
def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    cart_item, created = CartItem.objects.get_or_create(car=car, user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cars:car_list')

@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    order = Order.objects.create(user=request.user)
    order.cart_items.set(cart_items)

    # Making a request to car_warehouse API
    api_url = 'https://127.0.0.1/api/orders/'
    headers = {'Content-Type': 'application/json'}
    data = {
        'user': request.user.id,
        'items': [{'car_id': item.car.id, 'quantity': item.quantity} for item in cart_items],
    }
    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == status.HTTP_201_CREATED:
        cart_items.delete()
        return redirect('orders:order_success')
    else:
        return redirect('orders:order_failure')


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            context['cart_items'] = CartItem.objects.filter(user=user)
        else:
            context['cart_items'] = []
        return context

    
def order_success(request):
    return render(request, "order_success.html")

def order_failure(request):
    return render(request, "order_failure.html")
