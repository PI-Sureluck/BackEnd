from django.db import models

# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)
    xpath = models.CharField(max_length=500, null=True)

