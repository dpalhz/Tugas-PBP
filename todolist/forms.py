from django.forms import ModelForm
from .models import Task

class TodoListForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','isFinished']