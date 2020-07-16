from django.db import models


# Create your models here.

class Freelancer(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    username = models.CharField(max_length=45, null=False, blank=False, unique=True)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    biography = models.CharField(max_length=400, null=False, blank=False)
