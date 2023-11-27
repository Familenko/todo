from django.urls import path
from .views import TaskListView, TagListView


urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskListView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskListView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskListView.as_view(), name="task-delete"),


    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagListView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagListView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagListView.as_view(), name="tag-delete"),
]

app_name = "app"
