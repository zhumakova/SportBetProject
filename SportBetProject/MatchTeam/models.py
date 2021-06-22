from django.db import models

class Match(models.Model):
    team_a=models.ForeignKey("Team",on_delete=models.SET_NULL,null=True,related_name="team_a")
    team_b=models.ForeignKey("Team",on_delete=models.SET_NULL,null=True,related_name='team_b')
    status=models.CharField(max_length=20,choices=(
        ( 'soon', 'soon'),
    ('in process', 'in process'),
        ('closed','closed')

    ),default='soon')
    result=models.CharField(max_length=20,choices=(
        ('team_a','team_a'),
        ('team_b','team_b')
    ),blank=True)
    date=models.DateTimeField()

class Team(models.Model):
    title=models.CharField(max_length=20)
    year=models.PositiveIntegerField()
    total_games=models.PositiveIntegerField(default=0)
    wins=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
