# reminders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminders_list, name='reminders_list'),
    path('add/', views.add_reminder, name='add_reminder'),
    path('edit/<int:reminder_id>/', views.reminder_edit, name='reminder_edit'),
    path('delete/<int:reminder_id>/', views.reminder_delete, name='reminder_delete'),
    path('mark-done/<int:reminder_id>/', views.mark_done, name='mark_done'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
]