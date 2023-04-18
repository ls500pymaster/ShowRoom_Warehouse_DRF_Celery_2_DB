from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from DRF_CarDealer.apps.cars.models import Car
from .models import Order, CartItem
from .serializers import CartItemSerializer, OrderSerializer


class CartView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        car_id = request.data.get('car_id')
        quantity = request.data.get('quantity', 1)

        try:
            car = Car.objects.get(pk=car_id)
            cart_item, created = CartItem.objects.get_or_create(car=car, user=user)
            if not created:
                cart_item.quantity += quantity
            cart_item.save()

            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Car.DoesNotExist:
            return Response({"detail": "Car not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        user = request.user
        car_id = request.data.get('car_id')

        try:
            car = Car.objects.get(pk=car_id)
            cart_item = CartItem.objects.get(car=car, user=user)
            cart_item.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Car.DoesNotExist:
            return Response({"detail": "Car not found."}, status=status.HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({"detail": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)


class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items:
            return Response({"detail": "Your templates is empty."}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)
        order.cart_items.set(cart_items)
        order.save()

        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartTotalView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        total = sum(item.car.price * item.quantity for item in cart_items)

        return Response({"total": total})


def order_success(request):
    return render(request, "order_success.html")

def order_failure(request):
    return render(request, "order_failure.html")


@login_required
def order_summary(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'order_summary.html', {'cart_items': cart_items})

@login_required
def place_order(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        order = Order(user=request.user)
        order.save()
        order.cart_items.set(cart_items)
        order.save()
        cart_items.delete()
        return redirect('order_confirmation')
    return redirect('order_summary')


@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    context = {'order': order}
    return render(request, 'order_confirmation.html', context)