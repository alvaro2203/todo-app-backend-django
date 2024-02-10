from rest_framework import viewsets, status, exceptions, decorators
from .serializer import TaskSerializer, TagSerializer
from .models import Task, Tag
from rest_framework.response import Response

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        try:
            return Task.objects.all().order_by('last_modified')
        except Exception as e:
            raise exceptions.APIException(detail=str(e), code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TagView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    @decorators.action(detail=True, methods=['GET'])
    def tasks(self, request, pk=None):
        tag = self.get_object()
        tasks = tag.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        try:
            return Tag.objects.all().order_by('name')
        except Exception as e:
            raise exceptions.APIException(detail=str(e), code=status.HTTP_500_INTERNAL_SERVER_ERROR)