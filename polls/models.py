from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title



