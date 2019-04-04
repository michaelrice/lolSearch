from django.db import models
from taggit.managers import TaggableManager
from accounts.models import CustomUser


class Gif(models.Model):
    image_orig_url = models.URLField()
    image_200_url = models.URLField()
    image_id = models.TextField(max_length=128)
    image_tags = TaggableManager(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
