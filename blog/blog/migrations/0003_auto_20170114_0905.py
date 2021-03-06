# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20170114_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribers',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='subscriber',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Subscribers',
        ),
    ]
