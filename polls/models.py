from django.db import models

CATEGORY_CHOICES = [
    ('work', 'Work'),
    ('personal', 'Personal'),
    ('shopping', 'Shopping'),
    ('other', 'Other'),
]

CATEGORY_COLORS = {
    'work': '#007bff',
    'personal': '#28a745',
    'shopping': '#ffc107',
    'other': '#6c757d',
}

REPEAT_CHOICES = [
    ('none', 'No Repeat'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
]

class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    is_done = models.BooleanField(default=False)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    repeat = models.CharField(max_length=10, choices=REPEAT_CHOICES, default='none')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return self.title

    def category_color(self):
        return CATEGORY_COLORS.get(self.category, '#6c757d')


