# Generated by Django 2.0.3 on 2018-04-13 22:09

import caisse.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caisse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('number', models.CharField(max_length=3, validators=[caisse.models.validate_caisse_number], verbose_name='numéro')),
                ('liquidation_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email du service de liquidation')),
                ('active', models.BooleanField(default=False, verbose_name='activé')),
                ('score', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('caisse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caisse.Caisse')),
            ],
        ),
    ]
