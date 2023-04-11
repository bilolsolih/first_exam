from django.urls import path
from . import views

app_name = 'jobhunt'
urlpatterns = [
    path('stats/', views.StatisticsView.as_view(), name='stats')
]
