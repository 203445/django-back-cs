from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Profileimage(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    url_img = models.ImageField(null=True, upload_to='img_profile/')