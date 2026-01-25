from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def show(request):
    posts = Post.objects.all()
    return render(request, 'app/show.html', {'posts': posts})

@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})

def task_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        completed = request.POST.get("completed") 
        image = request.FILES.get("image")
        task = Task(title=title, description=description, completed=completed, image=image)
        task.save()  
        return redirect("task_list")
    return render(request, "task_add.html")

def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.completed = request.POST.get("completed")  
        task.image = request.FILES.get("image") 
        print(task.completed)
        task.save()
        return redirect("task_list")
    return render(request, "task_update.html", {"task": task})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

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
