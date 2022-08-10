from tkinter import CASCADE
from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import FloatField
from BakeryItem.models import Product
# Create your models here.



class Bill(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)#Foriegn key to fetch user detail
    product=models.ForeignKey(Product,on_delete=models.CASCADE)#Foriegn key to fetch products list
    quantity = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.user_id}"

    @property
    def amount(self):
        price=[float(x[0]) for x in Product.objects.filter(id=self.product.id).values_list('selling_price')]    
        for i in price:
            return self.quantity*i

      
