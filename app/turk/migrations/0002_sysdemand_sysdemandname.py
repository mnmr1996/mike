# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-17 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysdemand',
            name='sysDemandName',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
