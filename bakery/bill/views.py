from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import Bill
from .serializers import BillSerializer
from rest_framework.decorators import api_view,  authentication_classes, permission_classes
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
#To create bill and see all- Generic classes API
class BillCreateAPI(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def perform_create(self, serializer):
        user_id=serializer.validated_data.get('user_id')
        product=serializer.validated_data.get('product')
        quantity=serializer.validated_data.get('price')     
        serializer.save(user_id=user_id,quantity=quantity,product=product)

#Creating function from class so can be directly callable by view.py
bills = BillCreateAPI.as_view()



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
#To view specific bill in detail
class BillDetailAPIView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

#Creating function from class so can be directly callable by view.py
bill = BillDetailAPIView.as_view()



