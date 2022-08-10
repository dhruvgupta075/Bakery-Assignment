from rest_framework import serializers
from .models import Bill
from BakeryItem.models import Product
from BakeryItem.serializers import ProductSerializer

class BillSerializer(serializers.ModelSerializer):
    product=ProductSerializer
    class Meta:
        model = Bill
        fields = ['created', 'product', 'user_id', 'quantity','amount']
        depth=2


    