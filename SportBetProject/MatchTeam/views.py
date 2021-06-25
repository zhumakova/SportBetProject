from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Match,Team
from .serializers import MatchSerializer,TeamSerializer
from rest_framework import status
from .service import *

class MatchView(APIView):
    def get(self,request):
        match=Match.objects.all()
        serializer=MatchSerializer(match,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class TeamView(APIView):
    def get(self,request):
        team=Team.objects.all()
        serializer=TeamSerializer(team,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Counter(APIView):
    def put(self,request,**kwargs):
        m=Match.objects.get(id=kwargs['match_id'])
        b=m.bet_set.all()
        m.status='closed'
        m.save()
        team_a_bet=m.bet_set.filter(result='team_a').count()
        team_b_bet=m.bet_set.filter(result='team_b').count()
        for i in b:

            if m.result == 'team_a':
                coef = team_b_bet/team_a_bet
            else:
                coef=team_a_bet/team_b_bet
            if i.result==m.result:
                amount = i.amount
                amount=amount+(amount*coef)
                i.profile.wallet+=amount
                i.profile.save()
        return Response('Look at your wallet!',status=202)
