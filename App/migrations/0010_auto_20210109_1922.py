# Generated by Django 3.1.2 on 2021-01-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_army_moved'),
    ]

    operations = [
        migrations.AddField(
            model_name='hexes',
            name='name',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='hexes',
            name='water',
            field=models.BooleanField(default=False),
        ),
    ]
