# Generated by Django 2.1.10 on 2019-07-16 15:48

from django.db import migrations, models


def provision_user_number(apps, schema_editor):
    User = apps.get_model('mrsuser', 'User')
    for user in User.objects.all():
        if '_' not in user.username:
            continue

        user.number = user.username.split('_')[-1]
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mrsuser', '0007_superviseur'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=30, null=True, verbose_name="Numéro d'agent"),
        ),
        migrations.RunPython(provision_user_number),
    ]
