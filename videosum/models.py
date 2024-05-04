
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=16)
    video_file = models.FileField(upload_to='videos/')
