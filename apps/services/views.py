from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import ServicesListSerializer, ServicesDetailSerializer
from .models import Service, Feedback
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet


class ServicesListView(ListAPIView):
    serializer_class = ServicesListSerializer
    queryset = Service.objects.all()


class ServicesDetailView(RetrieveAPIView):
    serializer_class = ServicesDetailSerializer
    queryset = Service.objects.all()
    lookup_field = 'slug'


class FeedBackView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug, id, action):
        if action == 'create':
            service = get_object_or_404(Service, slug=slug)
            if request.user in service.rated_users:
                raise ValueError('Only one feedback per user per service')
            Feedback.objects.create(user=request.user, service=service, rating=request.POST.get('rating'), comment=request.POST.get('comment'))
            service.rated_users.add(request.user)

        elif action == 'delete':
            feedback = get_object_or_404(Feedback, id=id)
            if request.user != feedback.user:
                raise ValueError('Only the owner can delete the feedback')
            feedback.delete()
        else:
            raise ValueError('Action should be either create or delete')
