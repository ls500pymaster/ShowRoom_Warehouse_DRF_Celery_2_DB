from django import template

register = template.Library()

@register.filter(name='cart_total')
def cart_total(items):
    total = 0
    for item in items:
        total += item.car.price * item.quantity
    return total


@register.filter(name='car_item_total')
def car_item_total(item):
    return item.car.price * item.quantity