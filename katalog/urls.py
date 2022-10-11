# TODO: Implement Routings Here
from django.urls import path
from katalog.views import index

app_name = 'wishlist'

urlpatterns = [
    path('', index, name='show_katalog'),
]