# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drop_a_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(),
        ),
    ]