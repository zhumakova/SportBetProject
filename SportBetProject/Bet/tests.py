from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Bet
from django.urls import reverse
from MatchTeam.models import Match,Team
from userprofile.models import Profile

class BetTest(APITestCase):

    def setUp(self) -> None:

        self.team_a=Team.objects.create(title='A',year=2000,total_games=1,wins=1)
        self.team_b = Team.objects.create(title='B', year=2001, total_games=2, wins=1)
        self.match=Match.objects.create(team_a=self.team_a,team_b=self.team_b,
                                        status='soon',date='2021-06-30')
        self.user=User.objects.create_user(username='Bem',password='1234567')
        self.profile=Profile.objects.create(user=self.user,name='Bem',age=20,
                                            wallet=1000,promo_code='1234')
        self.url = reverse('bet',args=(self.match.id,))

    def test_bet_create(self):
        self.client.login(username='Bem',password='1234567')
        data={
            "result":"team_a",
            "amount":"500"
        }
        self.response=self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)