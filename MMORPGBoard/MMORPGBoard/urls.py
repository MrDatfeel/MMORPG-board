# MMORPGBoard/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('announcements/', include('announcements.urls')),  # Подключение маршрутов приложения
]

