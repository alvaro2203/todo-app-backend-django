from django.db import models

# Create your models here.
class Task(models.Model):

    STATE_CHOICES = {
        'pending': "pending",
        'doing': "doing",
        'done': "done",
    }

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default="pending")
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title