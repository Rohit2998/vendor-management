from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Vendor

from phonenumber_field.serializerfields import PhoneNumberField

class VendorSerializer(serializers.ModelSerializer):
    vendor_contact = serializers.CharField(source='get_vendor_contact', read_only=True)

    class Meta:
        model = Vendor
        # fields = ('username', 'password', 'email')  # Customize fields as needed
        # extra_kwargs = {'password': {'write_only': True}}  # Passwo
        # fields = '__all__'
        fields = ( 'vendor_name','vendor_address','vendor_contact','vendor_code')
    def get_vendor_contact(self, obj):
        return str(obj.vendor_contact)