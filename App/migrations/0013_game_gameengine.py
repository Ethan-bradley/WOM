# Generated by Django 3.1.2 on 2021-01-13 00:45

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_army_max_movement'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='GameEngine',
            field=picklefield.fields.PickledObjectField(default='', editable=False),
        ),
    ]
