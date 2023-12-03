from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vendor , PurchasedOrder

# from phonenumber_field.serializerfields import PhoneNumberField

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        # fields = ('username', 'password', 'email')  # Customize fields as needed
        # extra_kwargs = {'password': {'write_only': True}}  # Passwo
        # fields = '__all__'
        fields = ['vendor_name', 'vendor_address', 'vendor_contact', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate', 'vendor_code']

        # fields = ( 'vendor_name','vendor_address','vendor_contact','vendor_code','id','on_time_delivery_rate')
    # def get_vendor_contact(self, obj):
    #     return str(obj.vendor_contact)
    # def to_representation(self, instance):
    #     # Access the original representation of the instance
    #     representation = super().to_representation(instance)

    #     # Ensure that float fields are converted properly to strings
    #     float_fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    #     for field in float_fields:
    #         if field in representation and isinstance(representation[field], float):
    #             representation[field] = str(representation[field])
    #     print('asdasd',representation)
    #     return representation

class PurchasedOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedOrder
        # fields = ('username', 'password', 'email')  # Customize fields as needed
        # extra_kwargs = {'password': {'write_only': True}}  # Passwo
        fields = '__all__'
            # fields = ['vendor_name', 'vendor_address', 'vendor_contact', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate', 'vendor_code']
