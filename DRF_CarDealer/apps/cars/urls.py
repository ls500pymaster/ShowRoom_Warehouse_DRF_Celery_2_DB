from django.urls import path
from .views import CarDetailView, CarListView, CategoryListView, AboutPageView, IndexView

app_name = 'cars'

urlpatterns = [
	path("cars/", IndexView.as_view(), name="index"),
    path('<slug:slug>/', CarDetailView.as_view(), name='car_detail'),
	path("cars/", CarListView.as_view(), name="car_list"),
	path("about/", AboutPageView.as_view(), name="about"),
	path("categories/", CategoryListView.as_view(), name="category_list"),
]
