from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import CarQuantityViewSet

router = DefaultRouter()
router.register(r"cars", CarQuantityViewSet, basename="cars")

urlpatterns = [
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)