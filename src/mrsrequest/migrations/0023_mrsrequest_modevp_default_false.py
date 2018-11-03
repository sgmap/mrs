# Generated by Django 2.1.3 on 2018-11-03 20:38

from decimal import Decimal
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrsrequest', '0022_drop_mrsrequest_reject_template_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mrsrequest',
            name='modevp',
            field=models.BooleanField(blank=True, default=False, help_text='(Voiture, moto)', verbose_name='Avez vous voyagé en véhicule personnel ?'),
        ),
    ]
