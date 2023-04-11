from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('add/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
    path('order/', views.create_order, name='create_order'),
    path('success/', views.order_success, name='order_success'),
    path('failure/', views.order_failure, name='order_failure'),
]
