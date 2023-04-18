from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import TemplateView, ListView

from .models import Car, Category


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["category_list"] = Category.objects.all()
		return context


class CarDetailView(DetailView):
	model = Car
	context_object_name = "car"
	template_name = "car_detail.html"


class SearchResultsListView(ListView):
	model = Car
	context_object_name = "cars_list"
	template_name = "search_results.html"

	def get_queryset(self):
		query = self.request.GET.get("q")
		return Car.objects.filter(Q(model__icontains=query))


class AboutPageView(TemplateView):
	template_name = "about.html"


class CarListView(ListView):
	model = Car
	context_object_name = "car_list"
	template_name = "cars_list.html"


class CategoryListView(ListView):
	model = Category
	context_object_name = "category_list"
	template_name = "category_list.html"

