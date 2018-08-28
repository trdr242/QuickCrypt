# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-24 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptocoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('changehour', models.IntegerField()),
                ('changeday', models.IntegerField()),
                ('price', models.IntegerField()),
                ('cap', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
    ]