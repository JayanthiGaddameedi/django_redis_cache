from django.db import models

# Create your models here.


class Newsfeed(models.Model):
    news = models.CharField(max_length=255)