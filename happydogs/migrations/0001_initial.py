# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PeriodModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='dogmodel',
            name='date_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happydogs.PeriodModel'),
        ),
    ]
