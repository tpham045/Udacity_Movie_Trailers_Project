# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-14 20:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie_trailers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer_youtube_id',
            field=models.CharField(default=datetime.datetime(2017, 4, 14, 20, 39, 34, 147220, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
