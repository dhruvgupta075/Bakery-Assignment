from rest_framework import authentication,generics, mixins,permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view,  authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication
 
from rest_framework.permissions import IsAdminUser

class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
#Generic Classes API
#To see all products and add product
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        quantity=serializer.validated_data.get('quantity')
        price=serializer.validated_data.get('price')
        ingredients=serializer.validated_data.get('ingredients')        
        serializer.save(name=name,quantity=quantity,price=price,ingredients=ingredients)#Will save product entered by admin/owner if data is valid
        # Will send a Django signal
    

#Creating function from class so can be directly callable by view.py
product_list_create_view = ProductListCreateAPIView.as_view() 


#To retrive detail view of specfic product by its id
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'
product_detail_view = ProductDetailAPIView.as_view()


#Will lookup for product which needs to be updated
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save() #Will commit the changes made
        if not instance.name:
            instance.name = instance.name
            
#Creating function from class so can be directly callable by view.py
product_update_view = ProductUpdateAPIView.as_view()


#Will lookup for product which needs to be deleted
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

#Creating function from class so can be directly callable by view.py
product_destroy_view = ProductDestroyAPIView.as_view()
