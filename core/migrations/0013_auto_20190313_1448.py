# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-13 14:48
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190313_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default=1, max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]