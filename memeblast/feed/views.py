# Create your views here.
from django.shortcuts import render
from models import Picture
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
import datetime
#from django import forms

def feed(request):
    picture_list = Picture.objects.all().order_by('-posted_on')
    return render(request, 'feed.html', {
        "picture_list" : picture_list
    })

def edit_image(request):
    return render(request, 'upload.html', {})

def upload(request):
    if request.method == "POST":
        picture = Picture()
        picture.picture_url = request.POST['base64_image']
        picture.posted_on = datetime.datetime.now()
        picture.text = "testing hardstyle"
        picture.save()

        response_data = {}
        response_data['image_id'] = picture.pk

        return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
    else:
        return HttpResponseRedirect("/")

def publish(request):
    if request.method == "POST":
        picture = Picture.objects.get(pk = int(request.POST['image_id']))
        picture.published = True
        picture.save()
        
        response_data = {}
        respose_data = { "success" : True, "we_asked_for" : request.POST['image_id'] }
        return HttpResponse(simplejson.dumps(response_data), mimetype="application/json")
    else:
        return HttpResponseRedirect("/")