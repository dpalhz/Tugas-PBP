from django.urls import path
from mywatchlist.views import show_mywatchlist, show_json, show_xml

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
]