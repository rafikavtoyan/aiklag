# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 14:55
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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'floor',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('AP', 'Apartment'), ('HO', 'House'), ('CO', 'Commercial'), ('LA', 'Land')], default='AP', max_length=2)),
                ('publication_type', models.CharField(choices=[('SA', 'Sale'), ('MR', 'Monthly Rent'), ('DR', 'Daily Rent')], default='SA', max_length=2)),
                ('building_type', models.CharField(choices=[('PR', 'Partly Renovated'), ('ZS', 'Zero State'), ('GS', 'Gov State'), ('NO', 'Normal'), ('NR', 'Needs Some Repair'), ('OO', 'Old Overhaul'), ('OV', 'Overhaul'), ('NU', 'Newly Repaired Uninhabited'), ('RE', 'Renovation')], default='NO', max_length=2)),
                ('rooms', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('area', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100000), django.core.validators.MinValueValidator(1)])),
                ('heating', models.BooleanField(default=False)),
                ('gas', models.BooleanField(default=False)),
                ('hot_water', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('air_conditioner', models.BooleanField(default=False)),
                ('central_heating', models.BooleanField(default=False)),
                ('electricity', models.BooleanField(default=False)),
                ('standing_water', models.BooleanField(default=False)),
                ('water', models.BooleanField(default=False)),
                ('irrigation', models.BooleanField(default=False)),
                ('sewerage', models.BooleanField(default=False)),
                ('furniture', models.BooleanField(default=False)),
                ('equipment', models.BooleanField(default=False)),
                ('open_balcony', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('loggia', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('basement', models.BooleanField(default=False)),
                ('high_first_floor', models.BooleanField(default=False)),
                ('attic', models.BooleanField(default=False)),
                ('storage_room', models.BooleanField(default=False)),
                ('euro_windows', models.BooleanField(default=False)),
                ('tile', models.BooleanField(default=False)),
                ('heated_floor', models.BooleanField(default=False)),
                ('laminate_flooring', models.BooleanField(default=False)),
                ('Parquet', models.BooleanField(default=False)),
                ('sunny', models.BooleanField(default=False)),
                ('view', models.BooleanField(default=False)),
                ('close_to_the_bus_station', models.BooleanField(default=False)),
                ('roadside', models.BooleanField(default=False)),
                ('park', models.BooleanField(default=False)),
                ('playground', models.BooleanField(default=False)),
                ('garage', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('security_system', models.BooleanField(default=False)),
                ('Grating', models.BooleanField(default=False)),
                ('Heater', models.BooleanField(default=False)),
                ('fireplace', models.BooleanField(default=False)),
                ('building_existence', models.BooleanField(default=False)),
                ('gate', models.BooleanField(default=False)),
                ('fence', models.BooleanField(default=False)),
                ('bilateral', models.BooleanField(default=False)),
                ('iron_door', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('sauna', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('publisher', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.ForeignKey(blank=True, db_column='address', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Address')),
            ],
            options={
                'db_table': 'home',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=45, null=True)),
                ('home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Home')),
            ],
            options={
                'db_table': 'pictures',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'street',
            },
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'zip',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Building'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Floor'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Street'),
        ),
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Zip'),
        ),
    ]
