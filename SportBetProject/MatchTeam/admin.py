from django.contrib import admin
from .models import *

class MatchAdmin(admin.ModelAdmin):
    list_display = ['team_a','team_b','status','date','result']

admin.site.register(Match,MatchAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['title','year','total_games','wins']
admin.site.register(Team,TeamAdmin)

