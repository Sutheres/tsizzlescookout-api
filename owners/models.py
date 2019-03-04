from django.db import models


# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    instagram_name = models.CharField(max_length=200, blank=True)
    twitter_name = models.CharField(max_length=200, blank=True)
    current_participant = models.BooleanField(null=True)
    all_time_rank = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    owner = models.ForeignKey(Owner,related_name='seasons', on_delete=models.CASCADE)
    year = models.CharField(max_length=9)
    wins = models.IntegerField()
    losses = models.IntegerField()
    team_name = models.CharField(max_length=200)
    made_playoffs = models.BooleanField()
    playoff_wins = models.IntegerField()
    playoff_losses = models.IntegerField()
    made_superbowl = models.BooleanField()
    superbowl_wins = models.IntegerField()
    superbowl_losses = models.IntegerField()
    acquisitions = models.IntegerField()
    trades = models.IntegerField()

    def __str__(self):
        return self.year
