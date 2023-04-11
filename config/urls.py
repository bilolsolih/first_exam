from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobhunt/', include('apps.jobhunt.urls', namespace='jobhunt')),
    path('services/', include('apps.services.urls', namespace='services')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
