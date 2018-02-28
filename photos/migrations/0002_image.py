# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='categories/')),
                ('category', models.ManyToManyField(to='photos.Category')),
                ('location', models.ManyToManyField(to='photos.Location')),
            ],
        ),
    ]