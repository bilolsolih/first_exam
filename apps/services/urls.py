from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('main_page/', views.ServicesListView.as_view(), name='services_list'),
]
