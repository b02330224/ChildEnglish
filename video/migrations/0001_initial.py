# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('nums', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('store_path', models.CharField(default='', max_length=255)),
                ('num_views', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('e_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='video.Episode', verbose_name='Video')),
            ],
        ),
    ]
