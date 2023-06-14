# Generated by Django 3.1.2 on 2023-06-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0056_player_projection_unloaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphinterface',
            name='mode',
            field=models.CharField(choices=[('Income_Tax', 'Income Tax'), ('Corporate_Tax', 'Corporate Tax'), ('Welfare', 'Welfare'), ('Education', 'Education'), ('Science', 'Science'), ('Infrastructure', 'Infrastructure Spending'), ('Military', 'Military Spending'), ('MoneyPrintingArr', 'Money Printing'), ('Iron', 'Iron Prices'), ('Wheat', 'Wheat Prices'), ('Coal', 'Coal Prices'), ('Oil', 'Oil Prices'), ('Food', 'Food Prices'), ('ConsumerGoods', 'Consumer Goods Prices'), ('Steel', 'Steel Prices'), ('Machinery', 'Machinery Prices'), ('IronP', 'Iron Production'), ('WheatP', 'Wheat Production'), ('CoalP', 'Coal Production'), ('OilP', 'Oil Production'), ('FoodP', 'Food Production'), ('ConsumerGoodsP', 'Consumer Goods Production'), ('SteelP', 'Steel Production'), ('MachineryP', 'Machinery Production')], default='Income_Tax', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='CorporateTax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='Education',
            field=models.FloatField(default=0.01),
        ),
        migrations.AlterField(
            model_name='player',
            name='IncomeTax',
            field=models.FloatField(default=0.05),
        ),
        migrations.AlterField(
            model_name='player',
            name='InfrastructureInvest',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='player',
            name='Welfare',
            field=models.FloatField(default=0.0),
        ),
    ]