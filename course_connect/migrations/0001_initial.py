# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('img_path', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=datetime.datetime(2017, 2, 5, 8, 24, 47, 4554, tzinfo=utc))),
            ],
        ),
    ]
