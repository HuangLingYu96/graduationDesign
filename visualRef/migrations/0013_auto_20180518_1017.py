# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-18 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualRef', '0012_citation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('container_title', models.CharField(max_length=100)),
                ('page', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=3000)),
                ('is_referenced_by_count', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Citation',
        ),
    ]