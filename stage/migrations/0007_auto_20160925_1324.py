# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0006_auto_20160925_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='price',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Price'),
        ),
    ]
