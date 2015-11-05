from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Customer(models.Model):
    username = models.CharField('Username', max_length=30)
    fname = models.CharField('First Name', max_length=25)
    lname = models.CharField('Last Name', max_length=25)
    birth_date = models.DateField('Date of Birth')
    phone_number = models.IntegerField('Phone number')
    country = CountryField(blank_label='Choose country')
    city = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    confirm_password = models.CharField(max_length=25)

    def __unicode__(self):
       return '%s %s' %(self.fname, self.lname)


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="media/products/images", blank=True)
    product_price = models.FloatField()
    category = models.CharField(max_length=30)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(blank=True)

    def __unicode__(self):
       return '%s' %(self.product_name)


