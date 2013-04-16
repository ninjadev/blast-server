from django.conf.urls.defaults import *
import memeblast.feed.views as views
from memeblast.feed.api import PictureResource

picture_resource = PictureResource()

urlpatterns = patterns(
    '',
    url(r'^$', views.feed),
    url(r'^android/$', views.android),
    url(r'^iphone/$', views.iphone),
    url(r'^upload$', views.edit_image),
    url(r'^upload/post$', views.upload),
    url(r'^upload/publish$', views.publish),
    url(r'^api/', include(picture_resource.urls)),
)
