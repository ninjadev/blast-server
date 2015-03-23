from django.contrib import admin
from blast.feed.models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ('picture_url', 'posted_on', 'admin_image')

admin.site.register(Picture, PictureAdmin)
