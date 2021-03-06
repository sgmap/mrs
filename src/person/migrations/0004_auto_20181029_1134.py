# Generated by Django 2.1.2 on 2018-10-29 10:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_fix_y2k'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='nir',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(1000000000000, message='Le NIR doit contenir 13 caracteres.')], verbose_name='Numéro de sécurité sociale'),
        ),
    ]
