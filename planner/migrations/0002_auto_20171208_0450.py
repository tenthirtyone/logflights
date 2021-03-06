# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-08 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flightplan',
            name='payload_weight',
            field=models.FloatField(verbose_name='payload weight (kg)'),
        ),
        migrations.AlterField(
            model_name='telemetrymetadata',
            name='vehicle_type',
            field=models.IntegerField(choices=[(0, 'Not specified'), (1, 'Multicopter'), (2, 'Fixed Wing'), (3, 'VTOL')], default=0, verbose_name='vehicle type'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='empty_weight',
            field=models.FloatField(verbose_name='empty weight (kg)'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.IntegerField(choices=[(0, 'Not specified'), (1, 'Multicopter'), (2, 'Fixed Wing'), (3, 'VTOL')], default=0, verbose_name='vehicle type'),
        ),
    ]
