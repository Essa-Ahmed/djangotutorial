from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from .forms import ReminderForm

def get_theme(request):
    return request.session.get('theme', 'light')

def toggle_theme(request):
    current = get_theme(request)
    request.session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect('reminders_list')

def reminders_list(request):
    reminders = Reminder.objects.all()
    theme = get_theme(request)
    return render(request, 'polls/reminders_list.html', {
        'reminders': reminders,
        'theme': theme
    })

def reminder_create(request):
    theme = get_theme(request)
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reminders_list')
    else:
        form = ReminderForm()
    return render(request, 'polls/reminder_form.html', {
        'form': form,
        'theme': theme
    })

def reminder_edit(request, pk):
    theme = get_theme(request)
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminders_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'polls/reminder_form.html', {
        'form': form,
        'theme': theme
    })

def reminder_delete(request, pk):
    theme = get_theme(request)
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders_list')
    return render(request, 'polls/reminder_confirm_delete.html', {
        'reminder': reminder,
        'theme': theme
    })
