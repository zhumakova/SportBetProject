from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Match,Team
from .serializers import MatchSerializer,TeamSerializer
from rest_framework import status

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