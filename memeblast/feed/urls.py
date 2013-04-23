from django.conf.urls.defaults import *
import memeblast.feed.views as views
from tastypie.api import Api
from memeblast.feed.api import PictureResource

v1_api = Api(api_name='v1')
v1_api.register(PictureResource())

urlpatterns = patterns(
    '',
    url(r'^$', views.feed),
    url(r'^android/$', views.android),
    url(r'^iphone/$', views.iphone),
    url(r'^upload$', views.edit_image),
    url(r'^upload/post$', views.upload),
    url(r'^upload/publish$', views.publish),
    url(r'^api/', include(v1_api.urls)),
    url(r'^imageupload/', views.upload_image),
)
