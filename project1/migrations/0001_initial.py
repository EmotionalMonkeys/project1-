# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 18:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('is_bought', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sku', models.IntegerField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('role', models.CharField(choices=[(b'S', b'Seller'), (b'B', b'Buyer')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='order_shopping',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.User'),
        ),
        migrations.AddField(
            model_name='order_shopping',
            name='oSku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project1.Product'),
        ),
    ]
