from django.conf.urls import patterns, url
import feed.views as views

urlpatterns = patterns(
    '',
    url(r'^$', views.feed),
)
