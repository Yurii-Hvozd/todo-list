from django.urls import path
from todo.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskStatusView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("task/create", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete",
         TaskDeleteView.as_view(),
         name="task_confirm_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update",
         TagUpdateView.as_view(),
         name="tag_update"),
    path("tags/<int:pk>/delete",
         TagDeleteView.as_view(),
         name="tag_confirm_delete"),
    path("task/<int:pk>/toggle/",
         ToggleTaskStatusView.as_view(),
         name="toggle_task_status"),
]


app_name = "todo_list"
