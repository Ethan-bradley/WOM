# Generated by Django 4.2.2 on 2023-10-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0064_game_load_complete_game_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_started',
            field=models.BooleanField(default=False),
        ),
    ]