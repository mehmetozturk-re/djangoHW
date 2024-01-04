# Generated by Django 5.0 on 2023-12-25 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_aircraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='operator_airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_set', to='base.airline'),
        ),
    ]