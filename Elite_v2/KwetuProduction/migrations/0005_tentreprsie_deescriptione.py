# Generated by Django 5.0.6 on 2024-06-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KwetuProduction', '0004_tproduit_idcat_alter_tproduit_identrep'),
    ]

    operations = [
        migrations.AddField(
            model_name='tentreprsie',
            name='deescriptionE',
            field=models.TextField(blank=True, verbose_name="Description de l'entreprise"),
        ),
    ]
