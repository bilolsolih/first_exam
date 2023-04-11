from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('main_page/', views.ServicesListView.as_view(), name='services_list'),
    path('<slug:slug>/', views.ServicesDetailView.as_view(), name='services_detail'),
    path('<slug:slug>/feedbacks/<int:id>/<action>/', views.FeedBackView.as_view(), name='services_feedback'),
]
