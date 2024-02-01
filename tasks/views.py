from rest_framework import viewsets, status
from .serializer import TaskSerializer
from .models import Task
from rest_framework.response import Response

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        try:
            return Task.objects.all().order_by('last_modified')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)