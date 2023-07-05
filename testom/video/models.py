from django.db import models

# Create your models here.

class Video(models.Model):
    req_text = models.TextField()

class Video2(models.Model):
    req_text = models.TextField()
    time_video = models.IntegerField()
    fps = models.IntegerField()
    red = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()