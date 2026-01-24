from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", task_list, name="task_list"),
    path("task_add/",task_add, name="task_add"),
    path("task_delete/<int:task_id>", task_delete, name="task_delete"), 
    path("task_update/<int:task_id>",task_update, name="task_update"), 

    
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]


