# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171118_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(unique=True, upload_to='circular/')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(unique=True, upload_to='note/')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(unique=True, upload_to='poster/')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(unique=True, upload_to='practice_session/')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(unique=True, upload_to='question_paper/')),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='slider_image/')),
            ],
        ),
    ]
