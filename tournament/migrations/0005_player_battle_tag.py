# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_auto_20170424_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='battle_tag',
            field=models.CharField(default='#nameXXXX', max_length=256),
        ),
    ]
