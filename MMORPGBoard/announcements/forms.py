from django import forms
from django.contrib.auth.models import User
from .models import Announcement, Response

# Форма для регистрации пользователя
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")

# Форма для создания/редактирования объявления
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'category']  # Поля, которые будут доступны для редактирования

# Форма для отклика на объявление
class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['content']  # Поля, которые будут доступны для редактирования

