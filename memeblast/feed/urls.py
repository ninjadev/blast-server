from django.conf.urls import patterns, url
import memeblast.feed.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.feed),
    url(r'^android/$', views.android),
    url(r'^iphone/$', views.iphone),
    url(r'^upload$', views.edit_image),
    url(r'^upload/post$', views.upload),
    url(r'^upload/publish$', views.publish)
)
