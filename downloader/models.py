from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    download_location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
