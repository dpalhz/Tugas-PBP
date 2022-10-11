from unicodedata import name
from venv import create

from django.urls import path
from todolist.views import register, login_user, logout_user,show_todolist, create_task, delete_item, update_status, show_json, ajax_submit,show_model_fitur, update_status_ajax, delete_item_ajax

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('',show_todolist,name='show_todolist'),
    path('create-task/',create_task,name='create_task'),
    path('delete-item/<id>/', delete_item, name='delete_item'),
    path('update-status-item/<id>/', update_status, name='update_status'),
    path('json/', show_json, name='json'),
    path('add/',ajax_submit, name='modal'),
    path('model/',show_model_fitur, name='model'),
    path('model/delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('model/update-status-item-ajax/<int:id>/', update_status_ajax, name='update_status_ajax'),
]