from django.urls import path
from orders_and_payments import views

urlpatterns = [
    path('create-order/', views.CreateOrder.as_view(), name='order_create'),
    path('order-detail/<int:id>', views.OrderDetail.as_view(), name='order_detail'),
]