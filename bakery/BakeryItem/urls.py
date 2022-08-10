from django.urls import path

from . import views 

#inside /products/
urlpatterns = [
    path('products/', views.product_list_create_view, name='product-list'),
    path('products/<int:pk>/update', views.product_update_view, name='product-edit'),
    path('products/<int:pk>/delete', views.product_destroy_view,name= 'product-delete'),
    path('products/<int:pk>', views.product_detail_view, name='product-detail')
]
