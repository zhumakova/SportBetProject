# Generated by Django 3.2.4 on 2021-06-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MatchTeam', '0004_alter_match_result'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('dead', 'dead')], max_length=20)),
                ('bonus', models.IntegerField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.profile')),
                ('promo_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bet.promocode')),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('team_a', 'team_a'), ('team_b', 'team_b')], max_length=40)),
                ('amount', models.PositiveIntegerField(default=200)),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MatchTeam.match')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.profile')),
            ],
        ),
    ]
