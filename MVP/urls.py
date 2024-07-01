from django.urls import path
from MVP.api import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('process/', views.process, name='process'),
    path('download/<str:name>', views.download_file)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
