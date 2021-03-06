# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20170504_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='end_lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='road',
            name='end_long',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='road',
            name='middle_lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='road',
            name='middle_long',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='road',
            name='start_lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='road',
            name='start_long',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='road',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
