from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, throttling
from django.utils.text import slugify
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from tags.filters import StandardResultsSetPagination, CustomThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from products.models import Product
from products.serializers import ReadProductSerializer, CreateProductSerializer
from authentication.permissions import IsAdmin

class CreateProduct(APIView):
    
    permission_classes = (IsAdmin,)

    def post(self, request):
        create_serializer = CreateProductSerializer(data=request.data)
        if create_serializer.is_valid():
            name = create_serializer.validated_data.get('name')
            description = create_serializer.validated_data.get('price')
            price = create_serializer.validated_data.get('price')
            quantity = create_serializer.validated_data.get('quantity')
            tags = create_serializer.validated_data.get('tags')
            product_object = Product.objects.create(
                name=name,
                slug=slugify(name),
                description=description,
                price=price,
                quantity=quantity,
            )
            product_object.tags.set(tags)
            response_data = ReadProductSerializer(instance=product_object).data
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    lookup_field = "slug"
    
class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    pagination_class = StandardResultsSetPagination
    throttle_classes = (CustomThrottle, )
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name',]
    ordering_fields = ['created_at']
    filterset_fields = ['slug', 'price', 'quantity', 'tags']