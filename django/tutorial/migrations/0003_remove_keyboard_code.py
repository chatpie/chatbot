# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_keyboard_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyboard',
            name='code',
        ),
    ]
