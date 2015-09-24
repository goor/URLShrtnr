from django.db import models

# Create your models here.
class Urls(models.Model):
    id = models.SlugField(max_length=12,primary_key=True)
    url = models.URLField(max_length=256)
    short_date = models.DateTimeField(auto_now=True)
