# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-30 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0004_auto_20171029_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发表时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManage.User', verbose_name='Video')),
            ],
        ),
    ]
