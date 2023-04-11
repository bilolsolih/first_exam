from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import NoticeSerializer

from .models import Notice


class NoticesListView(ListAPIView):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all().order_by('-created')
    permission_classes = [AllowAny]


class NoticesDetailView(APIView):
    pass

# Create your views here.
