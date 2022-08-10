from rest_framework import serializers
from .models import Product

#Serializer for bakery item
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','quantity','cost_price','selling_price','ingredients']
        depth=1 #will print values inside ManyToMany field:ingredients