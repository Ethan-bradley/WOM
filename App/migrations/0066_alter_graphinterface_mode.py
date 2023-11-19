# Generated by Django 4.2.2 on 2023-11-19 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0065_game_game_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphinterface',
            name='mode',
            field=models.CharField(choices=[('Income_Tax', 'Income Tax'), ('Corporate_Tax', 'Corporate Tax'), ('Welfare', 'Welfare'), ('EducationSpend', 'Education'), ('Science', 'Science'), ('Infrastructure', 'Infrastructure Spending'), ('MilitarySpend', 'Military Spending'), ('InterestRate', 'Interest Rates'), ('Iron', 'Iron Prices'), ('Crops', 'Crop Prices'), ('Coal', 'Coal Prices'), ('Oil', 'Oil Prices'), ('Food', 'Food Prices'), ('Services', 'Services Prices'), ('Steel', 'Steel Prices'), ('Machinery', 'Machinery Prices'), ('IronP', 'Iron Production'), ('WheatP', 'Wheat Production'), ('CoalP', 'Coal Production'), ('OilP', 'Oil Production'), ('FoodP', 'Food Production'), ('ServicesP', 'Services Production'), ('SteelP', 'Steel Production'), ('MachineryP', 'Machinery Production')], default='Income_Tax', max_length=20),
        ),
    ]
