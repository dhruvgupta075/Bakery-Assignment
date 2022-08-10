from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name=models.CharField(max_length=30) #name of ingredient(Milk, egg)
    percentage=models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.percentage}%"


class Product(models.Model):
    name=models.CharField(max_length=20) #name of product(cake,pastry etc)
    quantity=models.IntegerField()
    selling_price=models.DecimalField(max_digits=6,decimal_places=2)
    cost_price=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    ingredients=models.ManyToManyField(Ingredient) # As one product may be made up of many fields

    def __str__(self):
        return f"{self.name}-{self.selling_price}"
    
   
