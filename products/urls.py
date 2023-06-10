from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.CreateProduct.as_view(), name='product_create'),
    path('detail/<str:slug>/', views.ProductDetails.as_view(), name='product_detail'),
    path('list/', views.ProductList.as_view(), name='products_list'),
         
]