from django.db import models

# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password1 = models.CharField(max_length=255)
    password2 = models.CharField(max_length=255)

