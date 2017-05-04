# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('created', models.DateField(auto_now=True)),
                ('completed', models.IntegerField(default=0)),
                ('lat', models.CharField(max_length=100)),
                ('longt', models.CharField(max_length=100)),
            ],
        ),
    ]