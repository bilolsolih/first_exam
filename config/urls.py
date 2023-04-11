from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobhunt/', include('apps.jobhunt.urls', namespace='jobhunt')),
]
