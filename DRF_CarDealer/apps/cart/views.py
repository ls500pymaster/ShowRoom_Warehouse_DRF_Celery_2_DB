from django.shortcuts import render, redirect, get_object_or_404
from DRF_CarDealer.apps.cars.models import Car
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, slug):
    car = get_object_or_404(Car, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(car=car, cart=cart)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart_detail.html', {'cart_items': cart_items})


@login_required
def remove_from_cart(request, slug):
    car = get_object_or_404(Car, slug=slug)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, car=car, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')


@login_required
def update_cart(request, slug):
    car = get_object_or_404(Car, slug=slug)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, car=car, cart=cart)
    quantity = int(request.POST.get('quantity'))
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('cart:cart_detail')
