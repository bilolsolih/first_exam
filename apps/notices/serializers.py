from rest_framework.serializers import ModelSerializer
from .models import Notice, Brand, CarModel


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'logo']


class CarModelSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['title']


class NoticeSerializer(ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    model = CarModelSerializer(many=False, read_only=True)

    class Meta:
        model = Notice
        fields = ['price', 'brand', 'model', 'get_average_price', 'get_difference']
