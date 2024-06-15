from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

posts = [
    {
        'author': 'Andy',
        'device': 'Xerox B415',
        'body': 'Body Text',
        'date_posted': 'June 14, 2024',
    },
    {
        'author': 'Joe',
        'device': 'Ricoh 4520',
        'body': 'Body Text',
        'date_posted': 'June 14, 2024',
    },

]


def inventory(request):
    context = {
        'posts': posts
    }
    return render(request, 'inventory/home.html', context)

def about(request):
    return render(request, 'inventory/about.html', {'title': 'About'})