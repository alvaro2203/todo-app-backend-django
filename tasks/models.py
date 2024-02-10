from django.db import models

# Create your models here.
class Tag(models.Model):

    TAG_COLORS = {
        "white": "white",
        "blue": "blue",
        "red": "red",
        "yellow": "yellow",
        "green": "green",
        "purple": "purple",
    }

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=10, choices=TAG_COLORS, default="white")

    def __str__(self):
        return self.name

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
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title