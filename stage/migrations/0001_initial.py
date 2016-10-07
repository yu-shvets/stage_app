# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField(null=True, verbose_name='Date of event')),
                ('artist_name', models.CharField(max_length=256, verbose_name="Artist's name")),
                ('event_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Name of event')),
                ('event_place', models.CharField(blank=True, default='', max_length=256, verbose_name='Place of event')),
                ('event_time', models.TimeField(null=True, verbose_name='Time of event')),
                ('poster', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Poster')),
                ('event_type', models.CharField(max_length=256, verbose_name='Type of event')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
            ],
        ),
    ]