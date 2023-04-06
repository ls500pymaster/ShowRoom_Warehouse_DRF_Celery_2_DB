from rest_framework import viewsets
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer


class CarQuantityViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

        # car_quantities = [{"id": car.id, "model": car.model, "warehouse count": car.warehouse_count,
        # "category": car.category} for car in queryset]
        # return Response(car_quantities)


class CarUpdateQuantityView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "id"

    def patch(self, request, *args, **kwargs):
        car = self.get_object()
        car.quantity = request.data.get("quantity")
        car.save()

        serializer = self.get_serializer(car)
        return Response(serializer.data)
