from django.db import models

# Create your models here.


class Site(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    logo = models.CharField(max_length=50)
    xpath = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    teamA = models.CharField(max_length=50)
    teamB = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Odds(models.Model):
    odd = models.FloatField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="odds")
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name="odds")


class SureBets(models.Model):
    teamA = models.CharField(max_length=50)
    teamB = models.CharField(max_length=50)
    oddA = models.FloatField()
    oddB = models.FloatField()
    profit = models.FloatField()
    site = models.ManyToManyField(Site, related_name="sites")
    event = models.ManyToManyField(Event, related_name="events")

