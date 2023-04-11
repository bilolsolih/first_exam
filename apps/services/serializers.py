from rest_framework.serializers import ModelSerializer
from .models import Service, Product, Feedback
from django.contrib.auth.models import User
from apps.profiles.models import Profile


class ServicesListSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['title', 'get_rating_for_listview']


class ProductNestedSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'discount']


class ProfileNestedSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_photo']


class UserNestedSerializer(ModelSerializer):
    profile = ProfileNestedSerializer(many=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'profile']


class FeedbackNestedSerializer(ModelSerializer):
    user = UserNestedSerializer(many=False, read_only=True)

    class Meta:
        model = Feedback
        fields = ['rating', 'comment', 'user']


class ServicesDetailSerializer(ModelSerializer):
    products = ProductNestedSerializer(many=True, read_only=True)
    feedbacks = FeedbackNestedSerializer(many=True)

    class Meta:
        model = Service
        fields = ['title', 'get_rating', 'products', 'feedbacks']
