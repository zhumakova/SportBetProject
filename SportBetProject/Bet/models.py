from django.db import models
from userprofile.models import Profile
from MatchTeam.models import Match


class Bet(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    match=models.ForeignKey(Match,on_delete=models.SET_NULL,null=True)
    result=models.CharField(max_length=40,choices=(
        ('team_a','team_a'),
        ('team_b','team_b')
    ))
    amount=models.PositiveIntegerField(default=200)

    def __str__(self):
        return self.profile.name

class Promocode(models.Model):
    code=models.CharField(max_length=4)
    status=models.CharField(max_length=20,choices=(
        ('active','active'),
        ('dead','dead')
    ),blank=True)
    bonus=models.IntegerField(default=500)

class Transaction(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    amount=models.PositiveIntegerField(default=0)
    promo_code=models.CharField(max_length=5)