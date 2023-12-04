from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import VendorSerializer
from .models import Vendor , PurchasedOrder
from django.http import JsonResponse
from .serializers import VendorSerializer , PurchasedOrderSerializer
import datetime
from rest_framework.decorators import api_view

class VendorAPIView(APIView):
    def get(self, request):
        queryset=Vendor.objects.filter()
        vendor_id = request.GET.get('id')
        serializer = VendorSerializer(queryset, many=True)
        all_vendors =  list(Vendor.objects.values_list('id', flat=True))
        all_purchased = PurchasedOrder.objects.filter()
        for i in all_vendors:
            all_purchased.filter(vendor=i)
            total = all_purchased.count()
            completed = all_purchased.filter(status = 'completed').count()
            fulfill =  completed /total
            Vendor.objects.filter(id  = i ).update(fulfillment_rate = fulfill*100)
        if vendor_id is not None:
            queryset=Vendor.objects.filter(id=int(vendor_id))
            serializer = VendorSerializer(queryset, many=True)

            serialized_data = serializer.data

            return JsonResponse(data =serialized_data,status =200,safe = False)
        
        serialized_data = serializer.data
        return JsonResponse(data =serialized_data,status =200,safe = False)
    
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to create a new instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


        today_date = datetime.date.today()
        vendor = request.data.get('vendor')
        try:
            vendor_change = Vendor.objects.get(id=vendor)
        except Vendor.DoesNotExist:
            data={'message':'invalid vendor'}
            return Response(data, status=404)


        instance.vendor=vendor_change
        instance.order_date=request.data.get('order_date')
        instance.delivery_date=request.data.get('delivery_date')
        instance.quantity=request.data.get('quantity')
        instance.quality_rating=request.data.get('quality_rating')
        instance.delivered_date = today_date
        deleiver_date  = datetime.datetime.strptime(instance.delivery_date , '%Y-%m-%d')

        if today_date <= deleiver_date.date() and instance.status == 'completed':
            instance.on_time = True
        instance.acknowledgment_date=request.data.get('acknowledgment_date')

        if request.data.get('status'):
            instance.status = request.data.get('status')
            print('')

        instance.save()            
        data={'message':'update successfully'}
        return Response(data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk): 
        try:
            instance = PurchasedOrder.objects.get(pk=pk)
        except PurchasedOrder.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])  # Specify the HTTP methods this view can handle
def order_acknowledge(request ,pk=None):
    if request.method == 'POST':        
        acknowledgment_date = request.data.get('acknowledge_date')
        issue_date = PurchasedOrder.objects.filter(id=pk)[0].issue_date

        if pk:
            ack_date =  datetime.datetime.strptime(acknowledgment_date , "%Y-%m-%dT%H:%M:%S")
            issue_date =  datetime.datetime.strptime(str(issue_date.replace(tzinfo=None)) , "%Y-%m-%d %H:%M:%S")
            resp_time = ack_date - issue_date
            vendor_id = PurchasedOrder.objects.filter(id=pk)[0].vendor.id
            v = Vendor.objects.filter(id=vendor_id)
            total_order  = PurchasedOrder.objects.filter(vendor=vendor_id).count()
            average_response_time = (v[0].average_response_time*total_order  + resp_time.days)/total_order
            v.update(average_response_time = average_response_time)
        return Response({"message": " acknowledged successfully"}, status=201)
        


