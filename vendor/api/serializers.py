from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vendor , PurchasedOrder

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = [ 'id','vendor_name', 'vendor_address', 'vendor_contact', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate', 'vendor_code']


class PurchasedOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedOrder
        fields = '__all__'
