from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import NoticeSerializer, NoticeListSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Notice


class NoticesListView(ListAPIView):
    serializer_class = NoticeListSerializer
    queryset = Notice.objects.all().order_by('-created')
    permission_classes = [AllowAny]


class NoticesDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        notice = get_object_or_404(Notice, id=id)
        serialized = NoticeSerializer(notice)
        return Response(serialized.data)

# Create your views here.
