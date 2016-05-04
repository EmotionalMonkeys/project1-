# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 08:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0003_auto_20160503_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_shopping',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
