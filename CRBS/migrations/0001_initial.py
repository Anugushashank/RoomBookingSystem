# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booking_date', models.DateTimeField(default=datetime.date.today)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('capacity', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.EmailField(unique=True, max_length=25)),
                ('password', models.CharField(max_length=20, null=True)),
                ('designation', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.ForeignKey(to='CRBS.Room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.ForeignKey(to='CRBS.UserData'),
        ),
    ]
