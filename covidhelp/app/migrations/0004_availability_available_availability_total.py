# Generated by Django 4.0.4 on 2022-05-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='available',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='availability',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
