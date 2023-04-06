"""DRF_CarDealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from DRF_CarDealer.apps.cars import views
from DRF_CarDealer.apps.cars.views import CategoryViewSet, CarViewSet, OrderViewSet, ClientViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"cars", CarViewSet, basename="cars")
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"users", ClientViewSet, basename="users")

urlpatterns = [
    path("", views.index, name="base"),
    path("admin/", admin.site.urls),
    # path('add/<slug:slug>/', views.add_car_to_cart, name='add_car_to_cart'),
    # path('cart/', views.cart_view, name='cart_view'),
    # path("swagger/", schema_view),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)