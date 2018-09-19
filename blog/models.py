from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField(default=None)
    image = models.ImageField(upload_to='images/')
