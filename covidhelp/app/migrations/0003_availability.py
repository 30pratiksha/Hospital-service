# Generated by Django 4.0.4 on 2022-05-14 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_facility_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilites', to='app.facility')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilites', to='app.hospital')),
            ],
        ),
    ]
