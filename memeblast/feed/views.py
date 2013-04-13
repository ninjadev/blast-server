# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Picture
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
import memeblast.settings.settings as settings
import datetime
import time
import random
#from django import forms

def android(request):
    return feed(request, "cordova.android.js")

def feed(request, cordova_js_file=""):
    picture_list = Picture.objects.all().order_by('+posted_on')
    return render(request, 'feed.html', {
        "picture_list" : picture_list,
        "cordova_js_file": cordova_js_file
    })

def edit_image(request):
    return render(request, 'upload.html', {})

@csrf_exempt
def upload(request):
    if request.method == "POST":
        
        filename = str(int(random.random() * 1000000)) + str(int(time.time())) + ".jpg"
        fh = open(settings.MEDIA_ROOT + filename , "wb")
        fh.write(request.POST['base64_image'].decode('base64'))
        fh.close()

        picture = Picture()
        picture.picture_url = filename
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
