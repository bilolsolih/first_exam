from django.contrib import admin
from .models import CarModel, Brand, Notice

admin.site.register(CarModel)
admin.site.register(Brand)
admin.site.register(Notice)
# Register your models here.
