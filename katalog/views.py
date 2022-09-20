from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def index(request):
    data = CatalogItem.objects.all()
    context = {
        'list_data': data,
        'nama':'Dipa Alhaza',
        'npm':'2106751543'
    }

    return render(request,'katalog.html',context)

