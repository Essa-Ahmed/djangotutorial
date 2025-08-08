from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminders_list, name='reminders_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('edit/<int:pk>/', views.reminder_edit, name='reminder_edit'),
    path('delete/<int:pk>/', views.reminder_delete, name='reminder_delete'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
]