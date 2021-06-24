from rest_framework import serializers
from .models import *

class BetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Bet
        fields='__all__'

class TransactionSerializer(serializers.Serializer):
    amount=serializers.IntegerField(min_value=200)
    promo_code=serializers.CharField(min_length=4)

