from django.urls import path
from .views import *

urlpatterns=[
    path('team/',TeamView.as_view()),
    path('match/',MatchView.as_view(),name='match'),
    path('counter/<int:match_id>/',Counter.as_view())
]