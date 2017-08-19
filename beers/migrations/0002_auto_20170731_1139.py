# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='beer',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='serving',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='beer',
            name='volume',
            field=models.CharField(choices=[(0.1, '0,1l'), (0.2, '0,2l'), (0.33, '0,33l'), (0.5, '0,5l'), (0.75, '0,75l'), (1, '1l')], default=0.5, max_length=10),
        ),
        migrations.AlterField(
            model_name='beer',
            name='plato',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
