from rest_framework import serializers
from .models import *

class MatchSerializer(serializers.ModelSerializer):
     team_a=serializers.StringRelatedField()
     team_b=serializers.StringRelatedField()
     class Meta:
         model=Match
         fields=['team_a','team_b','status','date']

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model=Team
        fields=['title','year','total_games','wins']