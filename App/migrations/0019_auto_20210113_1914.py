# Generated by Django 3.1.2 on 2021-01-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_auto_20210113_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='GoodsPerCapita',
            field=models.ImageField(default='default_graph.png', upload_to='graphs'),
        ),
    ]
