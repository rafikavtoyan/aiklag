from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Home(models.Model):
    # property type
    APARTMENT = 'AP'
    HOUSE = 'HO'
    COMMERCIAL = 'CO'
    LAND = 'LA'
    PROPERTY_TYPES = (
        (APARTMENT, 'Apartment'),
        (HOUSE, 'House'),
        (COMMERCIAL, 'Commercial'),
        (LAND, 'Land'),
    )
    property_type = models.CharField(
        max_length=2,
        choices=PROPERTY_TYPES,
        default=APARTMENT,
    )

    # publication type
    SALE = 'SA'
    MONTHLY_RENT = 'MR'
    DAILY_RENT = 'DR'
    PUBLICATION_TYPES = (
        (SALE, 'Sale'),
        (MONTHLY_RENT, 'Monthly Rent'),
        (DAILY_RENT, 'Daily Rent'),
    )
    publication_type = models.CharField(
        max_length=2,
        choices=PUBLICATION_TYPES,
        default=SALE,
    )

    # building type
    MONOLIT = 'MO'
    STONE = 'ST'
    PANEL = 'PA'
    OTHER = 'OT'
    NEW_CONSTRUCTION = 'NC'
    BUILDING_TYPES = (
        (MONOLIT, 'Monolit'),
        (STONE, 'Stone'),
        (PANEL, 'Panel'),
        (NEW_CONSTRUCTION, 'New Construction'),
        (OTHER, 'Other'),
    )
    building_type = models.CharField(
        max_length=2,
        choices=BUILDING_TYPES,
        default=STONE,
    )

    # Repair type
    PARTLY_RENOVATED = 'PR'
    ZERO_STATE = 'ZS'
    GOV_STATE = 'GS'
    NORMAL = 'NO'
    NEEDS_SOME_REPAIR = 'NR'
    OLD_OVERHAUL = 'OO'
    OVERHAUL = 'OV'
    NEWLY_REPAIRED_UNINHABITED = 'NU'
    RENOVATION = 'RE'
    REPAIR_TYPES = (
        (PARTLY_RENOVATED, 'Partly Renovated'),
        (ZERO_STATE, 'Zero State'),
        (GOV_STATE, 'Gov State'),
        (NORMAL, 'Normal'),
        (NEEDS_SOME_REPAIR, 'Needs Some Repair'),
        (OLD_OVERHAUL, 'Old Overhaul'),
        (OVERHAUL, 'Overhaul'),
        (NEWLY_REPAIRED_UNINHABITED, 'Newly Repaired Uninhabited'),
        (RENOVATION, 'Renovation'),
    )
    building_type = models.CharField(
        max_length=2,
        choices=REPAIR_TYPES,
        default=NORMAL,
    )

    rooms = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    price = models.DecimalField(max_digits=6, decimal_places=2)
    area = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100000),
            MinValueValidator(1)
        ]
    )
    # Facilities
    heating = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    central_heating = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    standing_water = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    irrigation = models.BooleanField(default=False)
    sewerage = models.BooleanField(default=False)

    # Additional information
    furniture = models.BooleanField(default=False)
    equipment = models.BooleanField(default=False)
    open_balcony = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    loggia = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    basement = models.BooleanField(default=False)
    high_first_floor = models.BooleanField(default=False)
    attic = models.BooleanField(default=False)
    storage_room = models.BooleanField(default=False)
    euro_windows = models.BooleanField(default=False)
    tile = models.BooleanField(default=False)
    heated_floor = models.BooleanField(default=False)
    laminate_flooring = models.BooleanField(default=False)
    Parquet = models.BooleanField(default=False)
    sunny = models.BooleanField(default=False)
    view = models.BooleanField(default=False)
    close_to_the_bus_station = models.BooleanField(default=False)
    roadside = models.BooleanField(default=False)
    park = models.BooleanField(default=False)
    playground = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    security_system = models.BooleanField(default=False)
    Grating = models.BooleanField(default=False)
    Heater = models.BooleanField(default=False)
    fireplace = models.BooleanField(default=False)
    building_existence = models.BooleanField(default=False)
    gate = models.BooleanField(default=False)
    fence = models.BooleanField(default=False)
    bilateral = models.BooleanField(default=False)
    iron_door = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)

    description = models.CharField(max_length=45, blank=True, null=True)
    publisher = models.CharField(max_length=45, blank=True, null=True)
    address = models.ForeignKey("Address", models.DO_NOTHING, db_column='address', blank=True, null=True)

    class Meta:
        db_table = 'home'


class Pictures(models.Model):
    url = models.CharField(max_length=45, blank=True, null=True)
    home = models.ForeignKey("Home", models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'pictures'


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

