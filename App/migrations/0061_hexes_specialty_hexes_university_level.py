# Generated by Django 4.2.2 on 2023-08-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0060_hexes_resentment'),
    ]

    operations = [
        migrations.AddField(
            model_name='hexes',
            name='specialty',
            field=models.CharField(choices=[('Fo', 'Food'), ('Ed', 'Education'), ('Cl', 'Clothes'), ('Se', 'Services'), ('Ho', 'Housing'), ('Co', 'Construction'), ('He', 'Healthcare'), ('Mi', 'Military'), ('ME', 'MedicalEquipment'), ('St', 'Steel'), ('Cr', 'Crops'), ('Ir', 'Iron'), ('Coa', 'Coal'), ('Oi', 'Oil'), ('Tr', 'Transport'), ('Ma', 'Machinery'), ('De', 'Deposits'), ('Ph', 'Physics'), ('Bi', 'Biology'), ('Ch', 'Chemistry')], default='Fo', max_length=3),
        ),
        migrations.AddField(
            model_name='hexes',
            name='university_level',
            field=models.IntegerField(default=1),
        ),
    ]
