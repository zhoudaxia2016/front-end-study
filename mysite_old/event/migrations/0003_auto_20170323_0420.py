# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-23 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20170323_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]