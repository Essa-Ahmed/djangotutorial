from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from .forms import ReminderForm
from django.db import models
from datetime import date

# 🌗 Theme toggle
def get_theme(request):
    return request.session.get('theme', 'light')

def toggle_theme(request):
    current = get_theme(request)
    request.session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect('reminders_list')

# 📋 Reminder list with search, sort, filter, and deadline color
def reminders_list(request):
    sort = request.GET.get('sort', 'date')
    filter_done = request.GET.get('filter', 'all')
    query = request.GET.get('q', '').strip()

    reminders = Reminder.objects.all()

    if filter_done == 'done':
        reminders = reminders.filter(is_done=True)
    elif filter_done == 'upcoming':
        reminders = reminders.filter(is_done=False)

    if query:
        reminders = reminders.filter(
            models.Q(title__icontains=query) |
            models.Q(description__icontains=query)
        )

    if sort == 'date':
        reminders = reminders.order_by('date', 'time')
    elif sort == 'title':
        reminders = reminders.order_by('title')

    for reminder in reminders:
        reminder_date = reminder.date.date() if hasattr(reminder.date, 'date') else reminder.date
        days_until = (reminder_date - date.today()).days
        if days_until == 0:
            reminder.deadline_color = '#dc3545'  # red
        elif 1 <= days_until <= 3:
            reminder.deadline_color = '#fd7e14'  # orange
        else:
            reminder.deadline_color = '#28a745'  # green

        category_colors = {
            'work': '#007bff',
            'personal': '#6f42c1',
            'urgent': '#e83e8c',
            'misc': '#20c997',
        }
        reminder.category_color = category_colors.get(reminder.category, '#888')

        # Optional: overdue detection
        # if reminder_date < date.today() and not reminder.is_done:
        #     reminder.deadline_color = '#6c757d'  # gray for overdue

    theme = get_theme(request)
    return render(request, 'polls/reminders_list.html', {
        'reminders': reminders,
        'theme': theme,
        'query': query
    })

# ➕ Add reminder
def add_reminder(request):
    theme = get_theme(request)
    if request.method == 'POST':
        form = ReminderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reminders_list')
    else:
        form = ReminderForm()
    return render(request, 'polls/add_reminder.html', {
        'form': form,
        'theme': theme
    })

# ✅ Mark as done
def mark_done(request, reminder_id):
    try:
        reminder = get_object_or_404(Reminder, pk=reminder_id)
        reminder.is_done = True
        reminder.save()
    except Exception as e:
        print("Error marking done:", e)
    return redirect('reminders_list')

# ✏️ Edit reminder
def reminder_edit(request, reminder_id):
    theme = get_theme(request)
    try:
        reminder = get_object_or_404(Reminder, pk=reminder_id)
    except Exception as e:
        print("Error loading reminder for edit:", e)
        return redirect('reminders_list')

    if request.method == 'POST':
        form = ReminderForm(request.POST, request.FILES, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminders_list')
    else:
        form = ReminderForm(instance=reminder)

    return render(request, 'polls/add_reminder.html', {
        'form': form,
        'theme': theme,
        'reminder': reminder
    })

# 🗑️ Delete reminder
def reminder_delete(request, reminder_id):
    try:
        reminder = get_object_or_404(Reminder, pk=reminder_id)
        reminder.delete()
    except Exception as e:
        print("Error deleting reminder:", e)
    return redirect('reminders_list')