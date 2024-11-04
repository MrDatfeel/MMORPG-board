# announcements/urls.py

from django.urls import path
from .views import create_announcement

urlpatterns = [
    path('create/', create_announcement, name='create_announcement'),
    # Другие маршруты...
]
