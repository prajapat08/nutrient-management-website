# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 09:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('content', models.CharField(max_length=1000)),
                ('publisher', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('article',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='articles.Article')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('article',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='articles.Article')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='users.User')),
            ],
        ),
    ]