# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0006_auto_20170731_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='plato',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
