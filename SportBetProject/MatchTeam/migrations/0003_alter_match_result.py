# Generated by Django 3.2.4 on 2021-06-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MatchTeam', '0002_alter_match_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(choices=[('team_a', 'team_a'), ('team_b', 'team_b')], max_length=20),
        ),
    ]
