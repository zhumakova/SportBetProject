from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField(default=18)
    wallet=models.PositiveIntegerField(default=0)
    promo_code=models.CharField(max_length=3)

    def __str__(self):
        return self.name


