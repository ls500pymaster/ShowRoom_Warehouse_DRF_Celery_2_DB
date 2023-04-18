from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def total_order_price(cart_items):
    return sum(item.car.price * item.quantity for item in cart_items)
