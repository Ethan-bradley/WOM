# Generated by Django 3.1.2 on 2021-01-16 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0021_policy_policygroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='game',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='App.game'),
        ),
    ]
