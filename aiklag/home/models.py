from __future__ import unicode_literals

from django.db import models


class Home(models.Model):
    rooms = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    publisher = models.CharField(max_length=45, blank=True, null=True)
    condition = models.ForeignKey("Condition", models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey("Address", models.DO_NOTHING, db_column='address', blank=True, null=True)

    class Meta:
        db_table = 'home'


class Pictures(models.Model):
    url = models.CharField(max_length=45, blank=True, null=True)
    home = models.ForeignKey("Home", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'pictures'


class Condition(models.Model):
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'condition'


class Address(models.Model):
    country = models.ForeignKey("Country", models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('City', models.DO_NOTHING, blank=True, null=True)
    zip = models.ForeignKey('Zip', models.DO_NOTHING, blank=True, null=True)
    street = models.ForeignKey('Street', models.DO_NOTHING, blank=True, null=True)
    building = models.ForeignKey('Building', models.DO_NOTHING, blank=True, null=True)
    floor = models.ForeignKey('Floor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'address'


class Country(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'Country'


class City(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'city'


class Zip(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'zip'


class Street(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'street'


class Building(models.Model):
    number = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'building'


class Floor(models.Model):
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'floor'

