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
from django.urls import path, include

from DRF_CarDealer.apps.cars.views import AboutPageView, CarListView, CategoryListView, IndexView
from DRF_CarDealer.apps.cars.views import CarDetailView, \
    SearchResultsListView
from DRF_CarDealer.apps.orders import views
from DRF_CarDealer.apps.users.views import SignupPageView
from DRF_CarDealer.apps.orders.views import *


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("cars/", CarListView.as_view(), name="car_list"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path('cars/<slug:slug>/', CarDetailView.as_view(), name='car_detail'),

    path('add/<slug:car_slug>/', views.add_to_cart, name='add_to_cart'),
    path("cart/", views.CartView.as_view(), name='cart'),

    path('search/', SearchResultsListView.as_view(), name='search_results'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)