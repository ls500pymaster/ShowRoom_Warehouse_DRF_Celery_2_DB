from django.contrib import admin
from .models import Car, Category, CategoryImage, CarImage


# Admin Customization
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("slug", "name",)
    list_filter = ("slug",)
    search_fields = ("name",)


# @admin.register(CategoryImage)
# class AdminCategoryImage(admin.ModelAdmin):
#     list_display = ("category",)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ("id", "model", "warehouse_count")
    list_filter = ("model", "torque", "fuel_type")
    search_fields = ("model", "engine", "drive_wheels")

#
# @admin.register(CarImage)
# class AdminCarImage(admin.ModelAdmin):
#     list_display = ("car",)



    def cars_list(self, obj):
        return ", ".join([str(car) for car in obj.cars.all()])

    cars_list.short_description = "Cars"