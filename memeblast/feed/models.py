from django.db import models
import memeblast.settings.settings as settings

class Picture(models.Model):
    picture_url = models.CharField(max_length=100)
    posted_on = models.DateTimeField()
    text = models.CharField(max_length=20, null=True, blank=True)
    published = models.BooleanField(default=False);

    def __unicode__(self):
        return str(self.pk) + " " + self.picture_url[:10]

    def get_absolute_url(self):
        return settings.MEDIA_URL + '/' + self.picture_url

    @staticmethod
    def get_latest(count=30):
        return Picture.objects.all().order_by('-posted_on')[:30]
