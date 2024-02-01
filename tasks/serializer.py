from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__" # fields = ("id", "title", "description", "done", ...)
        read_only_fields = ("id", "last_modified") # these fields cannot be updated by request