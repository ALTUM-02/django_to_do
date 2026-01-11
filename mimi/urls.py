from django.urls import path
from .views import *

urlpatterns = [
    path("", task_list, name="task_list"),
    path("task_add/",task_add, name="task_add"),
    path("task_delete/<int:task_id>", task_delete, name="task_delete"), 
    path("task_update/<int:task_id>",task_update, name="task_update"), 
]

#/<int:task_id"