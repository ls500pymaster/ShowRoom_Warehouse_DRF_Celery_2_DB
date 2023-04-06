from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = [
        ("suv", "SUV"),
        ('sedan', 'Sedan'),
        ('hybrid', 'Hybrid'),
        ("electric", "Electric"),
        ('performance', 'Performance'),
        ('future', 'Future'),
    ]
    name = models.CharField(max_length=15, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    engine = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    warehouse_count = models.PositiveIntegerField(default=0)
