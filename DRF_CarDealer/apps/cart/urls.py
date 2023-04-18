from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<slug:slug>/', views.update_cart, name='update_cart'),
    path('detail/', views.cart_detail, name='cart_detail'),
]
