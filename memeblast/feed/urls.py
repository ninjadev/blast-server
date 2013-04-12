from django.conf.urls import patterns,include,url
from feed.models import Picture
from feed import views

urlpatterns = patterns('',
        url(r'^$', 'views.whatever_function_you_want_to_use_to_display_shit'),
)
