from rest_framework.serializers import ModelSerializer
from .models import Service, Product, Feedback


class ProductNestedSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'discount']


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['title', 'get_rating']
