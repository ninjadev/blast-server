from django.db import models
import blast.settings.settings as settings

class Picture(models.Model):
    picture_url = models.CharField(max_length=100)
    posted_on = models.DateTimeField()
    text = models.CharField(max_length=20, null=True, blank=True)
    published = models.BooleanField(default=False);
    width = models.IntegerField(default=1024)
    height = models.IntegerField(default=1024)

    def __unicode__(self):
        return str(self.pk) + " " + self.picture_url[:10]

    def get_absolute_url(self):
        return settings.MEDIA_URL + '/' + self.picture_url

    def admin_image(self):
        return '<img src="%s" style="width:300px"/>' % self.get_absolute_url()
    admin_image.allow_tags = True

    @staticmethod
    def get_latest(count=30):
        return Picture.objects.all().order_by('-posted_on')[:30]
