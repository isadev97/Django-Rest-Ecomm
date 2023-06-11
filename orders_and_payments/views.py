from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import CreateTagSerializer, ReadTagSerializer
from tags.models import Tag
from rest_framework import status, throttling
from django.utils.text import slugify
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from tags.filters import StandardResultsSetPagination, CustomThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core.cache import cache
from tags.permissions import CustomPermission
from authentication.permissions import IsAdmin
from products.models import Product
from django.db import transaction
from orders_and_payments.models import Order, OrderItems
from orders_and_payments.serializers import ReadOrderDetailsSerializer


class CreateOrder(APIView):
    
    
    def fetch_product_price_and_quantity(self, item):
        key = list(item.keys())[0]
        id = int(key)
        product = Product.objects.get(pk=id)
        qty = item[key]
        return product, qty
    
    def get_total_amount(self, products_and_quantities):
        total_amount = 0
        for item in products_and_quantities:
                product, qty = self.fetch_product_price_and_quantity(item)
                total_amount += (product.price * qty)
        return total_amount
        
    def post(self, request):
        products_and_quantities = request.data.get('products_and_quantities')
        payment_mode = request.data.get('payment_mode')
        payment_status = request.data.get('payment_status')
        user = request.user
        with transaction.atomic():
            total_amount = self.get_total_amount(products_and_quantities)
            order = Order.objects.create(                
                    user=user,
                    payment_mode=payment_mode,
                    payment_status=payment_status,
                    payment_amount=total_amount
            )
            for item in products_and_quantities:
                product, qty = self.fetch_product_price_and_quantity(item)
                OrderItems.objects.create(
                    order=order,
                    product=product,
                    quantity_at_the_time_of_order=qty,
                    price_at_the_time_of_order=product.price
                )
        serializer_data = ReadOrderDetailsSerializer(instance=order).data
        return Response(serializer_data)
        
       
class OrderDetail(APIView):
    
    def get(self, request, id):
        order = Order.objects.get(pk=id)
        serializer_data = ReadOrderDetailsSerializer(instance=order).data
        return Response(serializer_data)
    
    
