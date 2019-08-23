# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 09:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_circular_note_poster_practicesession_questionpaper_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='workshop',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
