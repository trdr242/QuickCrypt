# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-28 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20180827_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocoin',
            name='changeday',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cryptocoin',
            name='changehour',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cryptocoin',
            name='changeweek',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cryptocoin',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cryptocoin',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
