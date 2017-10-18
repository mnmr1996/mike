# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-17 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_demand_Details', models.CharField(max_length=500)),
                ('bidder', models.CharField(max_length=50)),
                ('current_bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Uuid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('current_sys_damand', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('Dev_since', models.DateTimeField(auto_created=True)),
                ('Uuid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('wallet', models.IntegerField()),
                ('resume', models.FileField(upload_to='file path on system')),
                ('sysdemand', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SysDemand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_posted', models.DateTimeField(auto_now_add=True)),
                ('deadLine', models.DateTimeField(auto_now=True)),
                ('starting_price', models.IntegerField()),
                ('summary', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Posted', 'Posted'), ('Delivered', 'Delivered'), ('Timed-out', 'Timed-out'), ('Active', 'Active'), ('Canceled', 'Canceled'), ('None', 'None')], default='None', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ip_address', models.CharField(max_length=10)),
            ],
        ),
    ]