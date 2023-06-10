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

class CreateProduct(APIView):

    def post(self, request):
        pass
    
class ProductDetails(APIView):
    
    def get(self, request):
        pass 
    
class ProductList(ListAPIView):
    pass