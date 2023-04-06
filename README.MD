# In DRF_CarDealer directory
python manage.py runserver 8001

# In car_warehouse directory
python manage.py runserver 8000

# In DRF_CarDealer
celery -A DRF_CarDealer worker --loglevel=info
celery -A DRF_CarDealer beat --loglevel=info

DRF_CarDealer - is a store for car showroom.
Car_warehouse - is a warehouse with cars.


Car warehouse stock: http://127.0.0.1:8000/warehouse/cars/