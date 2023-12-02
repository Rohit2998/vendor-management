from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# from serializers import VendorSerializer
from .serializers import VendorSerializer
from .models import Vendor
from django.http import JsonResponse

from .serializers import VendorSerializer



# Create your views here.
def index(request):
    # return "hello"
    return HttpResponse("Hello index")

def index2(request):
    # return "hello"
    return HttpResponse("Hello index")
class VendorAPIView(APIView):
    def get(self, request):
        # pass
        data = {'message': 'This is a POST request'}
        # import ipdb;ipdb.set_trace()
        vendor_id = int(request.GET.get('id'))
        if vendor_id is not None:
            # import ipdb;ipdb.set_trace()
            queryset=Vendor.objects.filter(id=vendor_id)
            serializer = VendorSerializer(queryset, many=True)
            serialized_data = serializer.data
            # user=list(queryset.values())
            return JsonResponse(data =serialized_data,status =200,safe = False)

        return Response(data, status=status.HTTP_201_CREATED)
    def post(self, request):
        # import ipdb;ipdb.set_trace()
        name = request.data.get('name')
        address = request.data.get('name')
        phone = request.data.get('name')
        code = request.data.get('name')

        print('sa')
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to create a new instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response( data= {"message":"vendor created"})
    
# POST /api/vendors/: Create a new vendor.
# ● GET /api/vendors/: List all vendors.
# ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
# ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
# ● DELETE /api/vendors/{vendor_id}/: Delete a vendor.
# 1. Vendor Profile Management:
# ● Model Design: Create a model to store vendor information including name, contact
# details, address, and a unique vendor code.
# ● API Endpoints:
# ● POST /api/vendors/: Create a new vendor.
# ● GET /api/vendors/: List all vendors.
# ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
# ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
# ● DELETE /api/vendors/{vendor_id}/: Delete a vendor.
