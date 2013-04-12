from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # Feed urls
    url(r'^$', include('feed.urls')),

    # Examples:
    # url(r'^$', 'memeblast.views.home', name='home'),
    # url(r'^memeblast/', include('memeblast.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
