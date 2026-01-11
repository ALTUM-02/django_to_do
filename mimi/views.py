from django.shortcuts import render, redirect
from .models import Task


# Create your views here.


def show(request):
    posts = Post.objects.all()
    return render(request, 'app/show.html', {'posts': posts})

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
        print("(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))")
        print(task.completed)
        task.save()
        return redirect("task_list")
    return render(request, "task_update.html", {"task": task})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
