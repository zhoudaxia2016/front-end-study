# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-24 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('published_time', models.DateTimeField(verbose_name='Date publish')),
                ('comment_count', models.IntegerField(default=0)),
                ('view_num', models.IntegerField(default=0)),
            ],
        ),
    ]
