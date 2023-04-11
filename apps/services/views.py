from rest_framework.views import APIView
from .serializers import ServiceSerializer
from .models import Service
from rest_framework.generics import ListAPIView


class ServicesListView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

# Create your views here.
