# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0003_events_event_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['event_date'], 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='events',
            name='price',
            field=models.IntegerField(blank=True, max_length=5, null=True, verbose_name='Price'),
        ),
    ]
