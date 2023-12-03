from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import VendorSerializer
from .models import Vendor , PurchasedOrder
from django.http import JsonResponse
from .serializers import VendorSerializer , PurchasedOrderSerializer


class VendorAPIView(APIView):
    def get(self, request):
        # import ipdb;ipdb.set_trace()
        queryset=Vendor.objects.filter()
        vendor_id = request.GET.get('id')
        serializer = VendorSerializer(queryset, many=True)
        if vendor_id is not None:
            queryset=Vendor.objects.filter(id=int(vendor_id))
            serializer = VendorSerializer(queryset, many=True)
            serialized_data = serializer.data
            return JsonResponse(data =serialized_data,status =200,safe = False)
        serialized_data = serializer.data
        return JsonResponse(data =serialized_data,status =200,safe = False)
    
    def post(self, request):
        # import ipdb;ipdb.set_trace()
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to create a new instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response( data= {"message":"vendor created"})

    def put(self,request,pk=None):
        try:
            instance = Vendor.objects.get(id=pk)
        except Vendor.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        instance.vendor_name=request.data.get('vendor_name')
        instance.save()            
        data={'message':'update successfully'}
        return Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):  # 'pk' is the ID of the object to delete
        try:
            instance = Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



    
# POST /api/vendors/: Create a new vendor.
# ● GET /api/vendors/: List all vendors. done
# ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details. done
# ● PUT /api/vendors/{vendor_id}/: Update a vendor's details. done 
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


# 2. Purchase Order Tracking:

# ● API Endpoints:
# ● POST /api/purchase_orders/: Create a purchase order.
# ● GET /api/purchase_orders/: List all purchase orders with an option to filter by
# vendor.
# ● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
# ● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
# ● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.


class PurchasedOrderAPIView(APIView):
    def get(self, request,pk=None):
        # import ipdb;ipdb.set_trace()
        queryset=PurchasedOrder.objects.filter()
        if pk:
            queryset=PurchasedOrder.objects.filter(id=pk)
            serializer = PurchasedOrderSerializer(queryset, many=True)
            serialized_data = serializer.data
            return JsonResponse(data =serialized_data,status =200,safe = False)

        purchaseorder_id = request.GET.get('vendor')
        serializer = PurchasedOrderSerializer(queryset, many=True)
        if purchaseorder_id is not None:
            queryset=PurchasedOrder.objects.filter(vendor=int(purchaseorder_id))
            serializer = PurchasedOrderSerializer(queryset, many=True)
            serialized_data = serializer.data
            return JsonResponse(data =serialized_data,status =200,safe = False)
        serialized_data = serializer.data
        return JsonResponse(data =serialized_data,status =200,safe = False)
    
    def post(self, request):
        serializer = PurchasedOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to create a new instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        try:
            instance = PurchasedOrder.objects.get(id=pk)
        except PurchasedOrder.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)
        instance.po_number=request.data.get('po_number')
        vendor = request.data.get('vendor')
        vendor_change = Vendor.objects.get(id=vendor)
        instance.vendor=vendor_change
        instance.order_date=request.data.get('order_date')
        instance.delivery_date=request.data.get('delivery_date')
        instance.quantity=request.data.get('quantity')
        instance.quality_rating=request.data.get('quality_rating')
        instance.issue_date=request.data.get('issue_date')
        instance.acknowledgment_date=request.data.get('acknowledgment_date')

        instance.save()            
        data={'message':'update successfully'}
        return Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk): 
        try:
            instance = Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


