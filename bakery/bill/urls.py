from django.urls import path

from .views import *

urlpatterns = [
    path('bills/', bills, name="bill_list"),
    path('bills/<int:pk>', bill, name="bill_detail"),
]