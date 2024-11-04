from django.shortcuts import render, redirect
from .forms import AnnouncementForm

def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user  # Установите текущего пользователя как автора
            announcement.save()
            return redirect('announcement_list')  # Перенаправление на список объявлений
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create_announcement.html', {'form': form})

