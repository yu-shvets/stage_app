# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0005_auto_20160925_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='price',
            field=models.TextField(blank=True, null=True, verbose_name='Price'),
        ),
    ]
