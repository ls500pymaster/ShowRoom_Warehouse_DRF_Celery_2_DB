import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_CarDealer.settings')
app = Celery('DRF_CarDealer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.beat_schedule = {
#     'update_car_quantity_in_warehouse': {
#         'task': 'apps.cars.tasks.update_car_quantity_in_warehouse',
#         'schedule': timedelta(seconds=10),  # Run the task every 10 seconds
#     },
# }