from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    vendor_address = models.CharField(max_length=200)
    vendor_contact = models.CharField(max_length=200)
    quality_rating_avg = models.FloatField(blank=True, null= True, default=0.0)
    on_time_delivery_rate=models.FloatField(blank=True, null= True, default=0.0 )
    average_response_time = models.FloatField(blank=True, null= True, default=0.0)
    fulfillment_rate = models.FloatField(blank=True, null= True, default=0.0)
    vendor_code =  models.CharField(max_length=200 , unique=True, blank=False, null=False)
    def __str__(self):
        return self.vendor_name
class PurchasedOrder(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]
    po_number = models.CharField(max_length=200 ,unique=True, blank=False, null=False)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date= models.DateField()
    delivery_date = models.DateField()
    items = models.JSONField(max_length=200)
    quantity = models.IntegerField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    quality_rating = models.FloatField()
    issue_date = models.DateField()
    acknowledgment_date = models.DateField()
    
    def __str__(self):
        return self.po_number
    


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate =models.FloatField(blank=True, null= True, default=0.0 )
    quality_rating_avg = models.FloatField(blank=True, null= True, default=0.0 )
    average_response_time = models.FloatField(blank=True, null= True, default=0.0 )
    fulfillment_rate =models.FloatField(blank=True, null= True, default=0.0 )

    def __str__(self):
        return self.vendor


