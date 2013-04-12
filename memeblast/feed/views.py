# Create your views here.
from django.shortcuts import render
from models import Picture


def feed(request):
    picture_list = Picture.objects.all().order_by('-updated')
    return render(request, 'feed.html', {
        "picture_list" : picture_list
    })
