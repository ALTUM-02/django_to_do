from django.urls import path
from . import views
from .views import *

urlpatterns =[
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('tasks/', views.task_list, name='task_list'),
    path('task/add/', views.task_add, name='task_add'),
    path('task/delete/<int:id>/', views.task_delete, name='task_delete'),
    path('task/update/<int:id>/', views.task_update, name='task_update'),

]






