from .models import Task

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "_all_"        

