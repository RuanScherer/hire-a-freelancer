from django.db import models


# Create your models here.

class Freelancer(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    username = models.CharField(max_length=45, null=False, blank=False, unique=True)
    email = models.CharField(max_length=200, null=False, blank=False, unique=True)
    biography = models.CharField(max_length=400, null=False, blank=False)


class Contact(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    facebook = models.CharField(null=True, blank=True, max_length=250, unique=True)
    instagram = models.CharField(null=True, blank=True, max_length=250, unique=True)
    whatsapp = models.CharField(null=True, blank=True, max_length=15, unique=True)


class Rate(models.Model):
    rate_choices = [
        (1, 'BAD'),
        (2, 'MEDIUM'),
        (3, 'GOOD'),
        (4, 'AWESOME')
    ]
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    rate = models.IntegerField(null=False, blank=False, choices=rate_choices)
