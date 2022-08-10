from django.contrib import admin
from .models import Ingredient,Product
# Registering both models here.
admin.site.register(Product)
admin.site.register(Ingredient)