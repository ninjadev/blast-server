from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    # Feed urls
    url(r'^', include('blast.feed.urls')),

    # Examples:
    # url(r'^$', 'blast.views.home', name='home'),
    # url(r'^blast/', include('blast.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
