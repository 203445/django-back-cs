from django.db import models
from django.utils import timezone


# Create your models here.

#importación de forma directa
import datetime


class PrimerModelo(models.Model):
    campo_uno = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

class SegundpModelo(models.Model):
    campo_uno = models.CharField(max_length=255, null=True)
    edad = models.IntegerField(null=True, default=0)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'segundo_modelo'