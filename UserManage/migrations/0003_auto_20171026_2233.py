# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManage', '0002_auto_20171026_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
