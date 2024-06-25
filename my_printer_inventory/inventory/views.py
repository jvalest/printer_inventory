from django.shortcuts import render
from .models import inventory_entry, toner
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def inventory(request):
    context = {
        'posts': inventory_entry.objects.all()
    }
    return render(request, 'inventory/home.html', context)

def about(request):
    return render(request, 'inventory/about.html', {'title': 'About'})