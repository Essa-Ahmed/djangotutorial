# reminders/forms.py
from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'date', 'time', 'repeat', 'category', 'attachment']