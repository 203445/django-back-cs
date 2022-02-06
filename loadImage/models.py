from django.db import models
from django.utils import timezone
from distutils.command.upload import upload
# Create your models here.

#importación de forma directa
import datetime

class imageLoad(models.Model):
    name_img = models.CharField(max_length=255, null=False,)
    url_img = models.ImageField(null=False, upload_to='img/')
    format_img = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(default=timezone.now)
    edite = models.DateTimeField(blank=True, null=True, default=None)  
          