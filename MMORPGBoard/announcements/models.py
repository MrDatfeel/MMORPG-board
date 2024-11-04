from django.db import models
from django.contrib.auth.models import User

# Модель Announcement
class Announcement(models.Model):
    CATEGORY_CHOICES = [
        ('Танки', 'Танки'),
        ('Хилы', 'Хилы'),
        ('ДД', 'ДД'),
        ('Торговцы', 'Торговцы'),
        ('Гилдмастеры', 'Гилдмастеры'),
        ('Квестгиверы', 'Квестгиверы'),
        ('Кузнецы', 'Кузнецы'),
        ('Кожевники', 'Кожевники'),
        ('Зельевары', 'Зельевары'),
        ('Мастера заклинаний', 'Мастера заклинаний'),
    ]

    title = models.CharField(max_length=200)  # Заголовок объявления
    content = models.TextField()  # Содержимое объявления
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Категория объявления
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Внешний ключ к модели User
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания объявления
    updated_at = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления

    def __str__(self):
        return self.title

# Модель Response
class Response(models.Model):
    content = models.TextField()  # Содержимое отклика
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='responses')  # Внешний ключ к Announcement
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Внешний ключ к User
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания отклика

    def __str__(self):
        return f'Response to "{self.announcement.title}" by {self.user.username}'



