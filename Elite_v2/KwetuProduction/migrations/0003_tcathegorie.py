# Generated by Django 5.0.6 on 2024-06-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KwetuProduction', '0002_tentreprsie_tproduit_identrep'),
    ]

    operations = [
        migrations.CreateModel(
            name='tcathegorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCat', models.CharField(max_length=50, unique=True, verbose_name='Cathegorie')),
            ],
        ),
    ]
