from django.db import models
from django_resized import ResizedImageField


class Job(models.Model):
    image = ResizedImageField(size=[300, 300], upload_to='images/', crop=['middle', 'center'])
    summary = models.CharField(max_length=200)