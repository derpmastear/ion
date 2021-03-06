# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 02:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name='LDAPCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, unique=True)),
                ('section_id', models.CharField(max_length=10, unique=True)),
                ('course_title', models.CharField(blank=True, max_length=100)),
                ('course_short_title', models.CharField(blank=True, max_length=100)),
                ('teacher_name', models.CharField(blank=True, max_length=100)),
                ('room_name', models.CharField(blank=True, max_length=100)),
                ('term_code', models.CharField(blank=True, max_length=10)),
                ('period', models.IntegerField(max_length=10)),
                ('end_period', models.IntegerField(max_length=10)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],),
    ]
