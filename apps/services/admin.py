from django.contrib import admin
from .models import Service, Product, Feedback

admin.site.register(Feedback)


class ProductInline(admin.StackedInline):
    model = Product


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['title', 'created']


admin.site.register(Product)

# Register your models here.
