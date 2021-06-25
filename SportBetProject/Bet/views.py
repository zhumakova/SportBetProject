from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import *
from MatchTeam.models import Match
from .service import *
from userprofile.models import Profile


class BetPostView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            match=Match.objects.get(id=kwargs['match_id'])
        except Match.DoesNotExist:
            return Response('Does not exist!',status=404)
        if match.status!='soon':
            return Response('Match closed or live',status=404)
        try:
            profile=request.user.profile
        except Profile.DoesNotExist:
            return Response('Login or register!',status=404)
        serializer=BetSerializer(data=request.data)

        if serializer.is_valid():
            amount=serializer.data.get('amount')
            result=serializer.data.get('result')
            withdraw_money(amount,profile)
            Bet.objects.create(match=match,profile=profile,result=result,amount=amount)
            return Response("Successful!",status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=400)



class TransactionView(APIView):

    def post(self,request,*args,**kwargs):
        profile=request.user.profile
        serializer=TransactionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.data.get('amount')
            promo_code=serializer.data.get('promo_code')
            try:
                check=Promocode.objects.get(code=promo_code).bonus
                print(check)
            except Promocode.DoesNotExist:
                check=0
            profile.wallet+=amount+check
            profile.save()

            Transaction.objects.create(amount=amount,promo_code=promo_code,profile=profile)
            return Response('Successful!',status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


