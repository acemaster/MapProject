# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20170504_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='road',
            name='remarks',
            field=models.TextField(default='None', max_length=400),
        ),
    ]