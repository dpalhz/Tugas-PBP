from unicodedata import name
from venv import create
from django.urls import path
from todolist.views import register, login_user, logout_user,show_todolist, create_task, delete_item, update_status

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('',show_todolist,name='show_todolist'),
    path('create-task/',create_task,name='create_task'),
    path('delete-item/<id>/', delete_item, name='delete_item'),
    path('update-status-item/<id>/', update_status, name='update_status')
]