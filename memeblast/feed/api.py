from memeblast.feed.models import Picture
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

class PictureResource(ModelResource):
    fields = ['picture_url', 'posted_on']

    class Meta:
        queryset = Picture.objects.all().order_by('-posted_on')
        resource_name = 'pictures'
