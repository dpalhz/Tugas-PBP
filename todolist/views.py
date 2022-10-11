from django.shortcuts import render
from . import forms

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse

from .models import Task



# def create_tast(request):
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todoList = Task.objects.all()
    todoList = todoList.filter(user=request.user)

    context = {
    'todoList' : todoList,
    'last_login': request.COOKIES['last_login'],
}
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = forms.TodoListForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('todolist:show_todolist')
    else:
        form = forms.TodoListForm()
    context = {
        'form': form,
        'last_login': request.COOKIES['last_login']
    }
    return render(request,'create_task.html',context)


def delete_item(request,id):
    form = Task.objects.filter(pk=id)
    form.delete()
    return redirect('todolist:show_todolist')


def update_status(request, id):
    obj = Task.objects.get(pk=id)
    obj.isFinished^=True
    obj.save()
    return redirect('todolist:show_todolist')


def show_json(request):
    data = Task.objects.all()
    task_item = data.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task_item), content_type="application/json")

def ajax_submit(request):
    if (request.method == 'POST'):
        user = request.user
        data = {}
        form = forms.TodoListForm(request.POST or None)
        if (form.is_valid()):
            title = form.cleaned_data['title']
            deskripsi = form.cleaned_data['description']
            isFinished = form.cleaned_data['isFinished']
            new_data = Task.objects.create(user=user, title=title, description=deskripsi, isFinished=isFinished)
            data["title"] = title
            data["description"] = deskripsi
            data["isFinished"] = isFinished
            data["pk"] = new_data.pk
            data["date"] = new_data.date
            new_data.save()
            return JsonResponse(data)

def delete_item_ajax(request,id):
    form = Task.objects.filter(pk=id)
    form.delete()
    return HttpResponseRedirect(reverse('todolist:model'))


def update_status_ajax(request, id):
    obj = Task.objects.get(pk=id)
    obj.isFinished^=True
    obj.save()
    return HttpResponseRedirect(reverse('todolist:model'))
    

def show_model_fitur(request):
    return render(request,'todolist_modelAjax.html')