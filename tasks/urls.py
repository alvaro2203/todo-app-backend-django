from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks.views import TaskView, TagView

task_router = routers.DefaultRouter()
tag_router = routers.DefaultRouter()

task_router.register(r'tasks', TaskView, 'tasks')
tag_router.register(r'tags', TagView, 'tags')

urlpatterns = [
    path("api/v1/", include(task_router.urls)),
    path("api/v1/", include(tag_router.urls)),
    path("docs/", include_docs_urls(title="Tasks API"))
]
