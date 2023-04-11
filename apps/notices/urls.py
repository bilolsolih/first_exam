from django.urls import path
from . import views

app_name = 'notices'
urlpatterns = [
    path('', views.NoticesListView.as_view(), name='notices_list'),
    path('<int:id>/', views.NoticesDetailView.as_view(), name='notices_detail'),

]
