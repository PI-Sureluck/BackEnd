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
    team = models.CharField(max_length=50)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="odds")
    event = models.ForeignKey(Event,on_delete=models.CASCADE, related_name="odds")

    def __str__(self):
        return f"{self.team} - ODD: {self.odd}"


class SureBets(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    teamA = models.CharField(max_length=50)
    teamB = models.CharField(max_length=50)
    oddA = models.ForeignKey(Odds,on_delete=models.CASCADE, related_name="odds_a")
    oddB = models.ForeignKey(Odds,on_delete=models.CASCADE, related_name="odds_b")
    profit = models.FloatField()

    def __str__(self):
        return f"{self.teamA} X {self.teamB}"


