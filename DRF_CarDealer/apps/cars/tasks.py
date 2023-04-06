import requests
from celery import shared_task
from DRF_CarDealer.apps.cars.models import Car, Category


@shared_task
def update_car_quantity_in_warehouse():
    response = requests.get("http://127.0.0.1:8000/warehouse/cars/")
    car_quantities = response.json()

    for car_data in car_quantities:
        car_id = car_data["id"]
        car_model = car_data["model"]
        warehouse_count = car_data["warehouse_count"]

        try:
            car = Car.objects.get(id=car_id)
            car.warehouse_count = warehouse_count
            car.save()
        except Car.DoesNotExist:
            print("Car not found")
            pass


@shared_task()
def add_new_car_models():
    response = requests.get("http://127.0.0.1:8000/warehouse/cars/")
    new_car_model = response.json()

    for car_data in new_car_model:
        car_id = car_data["id"]
        car_model = car_data["model"]
        car_category = car_data["category"]["name"]
        warehouse_count = car_data["warehouse_count"]
        car_price = car_data["price"]
        car_category, _ = Category.objects.get_or_create(name=car_category)

        car, created = Car.objects.get_or_create(id=car_id, defaults={
            'model': car_model,
            'category': car_category,
            'warehouse_count': warehouse_count,
            'price': car_price
        })