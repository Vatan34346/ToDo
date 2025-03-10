from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'TO-DO'),
        ('in_progress', 'In-Progress'),
        ('done', 'Done')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    create_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
