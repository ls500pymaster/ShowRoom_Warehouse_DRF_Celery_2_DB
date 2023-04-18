from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, OrderCreateView

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    path('api/orders/', OrderCreateView.as_view(), name='orders_create'),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)