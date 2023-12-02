from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
# class 

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    vendor_address = models.CharField(max_length=200)
    # vendor_contact = PhoneNumberField(default_region='IN')
    vendor_contact = PhoneNumberField(region='IN')
    
    vendor_code =  models.CharField(max_length=200 , unique=True, blank=False, null=False)
    def __str__(self):
        return self.vendor_name
    
    # name, contact
# details, address, and a unique vendor code.