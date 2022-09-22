from django.shortcuts import render
from mywatchlist.models import FilmItem

from django.http import HttpResponse
from django.core import serializers


def show_json(request):
    data = FilmItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = FilmItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


# Create your views here.
def show_mywatchlist(request):
    data_film_mywatchlist = FilmItem.objects.all()
    counObj = len(data_film_mywatchlist)
    cnt = 0
    pesan = ""
    for x in data_film_mywatchlist:
        if x.watched == True:
            cnt += 1
    
    if cnt >= counObj - cnt:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"
    
    context = {
        'list_film': data_film_mywatchlist,
        'nama': 'Dipa Alhaza',
        'npm': '2106751543',
        'pesan': pesan

    }
    return render(request,'mywatchlist.html',context)