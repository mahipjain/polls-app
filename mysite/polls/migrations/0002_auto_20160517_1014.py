# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='chioce_text',
            new_name='choice_text',
        ),
    ]
