from django.conf.urls import patterns, url
from django import forms
import feed.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.feed),
    url(r'^upload$', views.edit_image),
    url(r'^upload/post$', views.upload),
    url(r'^upload/publish$', views.publish)
)
