from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=200)
    vendor_address = models.CharField(max_length=200)
    vendor_contact = models.CharField(max_length=200)
    quality_rating_avg = models.FloatField(blank=True, null=True, default=0.0)
    on_time_delivery_rate = models.FloatField(
        blank=True, null=True, default=0.0
    )
    average_response_time = models.FloatField(
        blank=True, null=True, default=0.0
    )
    fulfillment_rate = models.FloatField(blank=True, null=True, default=0.0)
    vendor_code = models.CharField(
        max_length=200, unique=True, blank=False, null=False
    )

    def __str__(self):
        return self.vendor_name


class PurchasedOrder(models.Model):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELED = "canceled"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
    ]
    po_number = models.CharField(
        max_length=200, unique=True, blank=False, null=False
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField()
    delivered_date = models.DateField(blank=True, null=True)
    on_time = models.BooleanField(default=False)
    items = models.JSONField(max_length=200)
    quantity = models.IntegerField(max_length=200)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PENDING
    )
    quality_rating = models.FloatField(blank=True, null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.po_number


@receiver(post_save, sender=PurchasedOrder)
def update_fields(sender, instance, created, **kwargs):
    if instance.status == "completed":
        # import ipdb;ipdb.set_trace()
        rating = instance.quality_rating
        v = Vendor.objects.filter(id=instance.vendor_id)
        purchased_per_vendor = PurchasedOrder.objects.filter(
            vendor=instance.vendor_id
        ).count()
        quality_rating_avg = (
            v[0].quality_rating_avg * (purchased_per_vendor - 1) + rating
        ) / purchased_per_vendor
        v.update(quality_rating_avg=quality_rating_avg)
        total_completed_order = PurchasedOrder.objects.filter(
            vendor=instance.vendor_id, status="completed"
        )
        on_time = PurchasedOrder.objects.filter(
            vendor=instance.vendor_id, status="completed", on_time=True
        )
        on_time_delivery_rate_new = (
            (on_time.count()) / total_completed_order.count()
        ) * 100
        v.update(on_time_delivery_rate=on_time_delivery_rate_new)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateField()
    on_time_delivery_rate = models.FloatField(
        blank=True, null=True, default=0.0
    )
    quality_rating_avg = models.FloatField(blank=True, null=True, default=0.0)
    average_response_time = models.FloatField(
        blank=True, null=True, default=0.0
    )
    fulfillment_rate = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self):
        return self.vendor
