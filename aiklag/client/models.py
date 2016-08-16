from __future__ import unicode_literals

from django.db import models
from django.db import models
from django import forms
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


class AiklagUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, last_name, gender, phone_number, location,
                    password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must provide first name')
        if not last_name:
            raise ValueError('Users must provide last name')
        if not date_of_birth:
            raise ValueError('Users must provide date of birth')
        if not gender:
            raise ValueError('Users must provide gender')
        if not phone_number:
            raise ValueError('Users must provide a phone number')
        if not location:
            raise ValueError('Users must provide his/her location')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number,
            location=location
        )
        if not password or not password2:
            raise ValueError("You must confirm your password")
        if password != password2:
            raise ValueError("Your passwords do not match")

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, first_name, last_name, gender, phone_number, location,
                         password=None, password2=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            date_of_birth=date_of_birth,
            password=password,
            password2=password2,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number,
            location=location
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class AiklagUser(AbstractBaseUser):
    GENDER_CHOICE = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    first_name = models.CharField(
        verbose_name="first name",
        max_length=70,
    )
    last_name = models.CharField(
        verbose_name="last name",
        max_length=70,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICE
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)  # validators should be a list
    location = CountryField()
    objects = AiklagUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


