# Generated by Django 2.0 on 2017-12-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=200, verbose_name='Nom de famille')),
                ('birth_date', models.DateField(null=True, verbose_name='Date de naissance')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('nir', models.IntegerField(verbose_name='Numéro de sécurité sociale')),
            ],
            options={
                'verbose_name': 'Personne',
                'ordering': ('last_name', 'first_name'),
            },
        ),
    ]
