from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.def create_task(request):


def create_task(request):
    if request.method == "Task":
        title = request.Task['title']
        Task.objects.create(
            user=request.user,  
            title=title
        )
        return redirect('task_list')

@login_required(login_url='login')   
def task_detail(request,id):
    task = get_object(Task, id=id, user=request.user)
    return render(request, "tasks/task_detail.html", {"task": task})     

def show(request):
    Tasks = Task.objects.all()
    return render(request, 'app/show.html', {'Tasks': Tasks})

@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "task_list.html", {"tasks": tasks})

@login_required
def task_add(request):
    if request.method == "Task":
        form = TaskForm(request.Task, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.ser
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "task_add.html", {"form": form})

@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == "Task":
        task.title = request.Task.get("title")
        task.description = request.Task.get("description")
        task.completed = request.Task.get("completed")  
        task.image = request.FILES.get("image") 
        print(task.completed)
        task.save()
        return redirect("task_list")
    return render(request, "task_update.html", {"task": task})

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "Task":
        username = request.Task.get('username')
        email = request.Task.get('email')
        password1 = request.Task.get('password1')
        password2 = request.Task.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "Task":
        username = request.Task.get('username')
        password = request.Task.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, "Invalid login details")
            return redirect('login')

        pass

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
