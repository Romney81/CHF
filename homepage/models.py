
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse, HttpResponseRedirect, Http404

class SiteUser(AbstractUser):
	address = models.CharField(max_length=60, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=12, blank=True, null=True)
	zip_code = models.IntegerField(max_length=5, blank=True, null=True)
	phone = models.CharField(max_length=30, blank=True, null=True)
	account_balance = models.IntegerField(blank=True, null=True)


class Product(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=144)
	category = models.CharField(max_length=144)
	current_price = models.DecimalField(max_digits=6,decimal_places=2, null=True)
	is_active = models.NullBooleanField(default=True, blank=True, null=True)

	def __str__(self):
		return self.name


class Location(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=30, blank=True, null=True)
	is_active = models.NullBooleanField(default=True, blank=True, null=True)

	def __str__(self):
		return self.name


class Item(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	description = models.CharField(max_length=144, blank=True, null=True)
	value = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	is_rentable = models.NullBooleanField(default=True,blank=True, null=True)
	is_active = models.NullBooleanField(default=True, blank=True, null=True)

	def __str__(self):
		return self.name

class WardrobeItem(models.Model):
    size = models.CharField(max_length=2)
    size_modifier = models.CharField(max_length=30)
    gender = models.BooleanField(default=True)
    color = models.CharField(max_length=30)
    pattern = models.CharField(max_length=30)
    start_year = models.DateField()
    end_year = models.DateField()
    note = models.CharField(max_length=255)
    is_rentable = models.BooleanField(default=False)

class Area(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

class Event(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)
	location = models.CharField(max_length=255)
	is_active = models.NullBooleanField(default=True, blank=True, null=True)

	def __str__(self):
		return self.name

class Rentals(models.Model):
	name = models.CharField(max_length=30)
	rental_date = models.DateField(blank=True, null=True)
	due_date = models.DateField(blank=True, null=True)
	person = models.ForeignKey(SiteUser, null=True)
	new_damage = models.CharField(max_length = 1000)
	was_returned = models.NullBooleanField(default = False, blank = True, null = True)

	def __str__(self):
		return self.person.first_name

class Purchases(models.Model):
	customer = models.ForeignKey(SiteUser, null=True)
	total = models.DecimalField(max_digits=6,decimal_places=2, null=True)
	purchase_date = models.DateField(blank=True, null=True)
	charge_id = models.CharField(max_length=200)
