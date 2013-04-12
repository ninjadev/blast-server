from django.db import models

class Picture(models.Model):
    picture_url = models.CharField(max_length=100)
    posted_on = models.DateTimeField()
    text = models.CharField(max_length=20, null=True, blank=True)