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

class CreateTag(APIView):

    def post(self, request):
        print("authentication user", request.user)
        # serializer for incoming data
        create_serializer = CreateTagSerializer(data=request.data)
        if create_serializer.is_valid():
            name = create_serializer.validated_data.get('name')
            tag_object = Tag.objects.create(
                name=name,
                slug=slugify(name)
            )
            # serializer for outgoing data
            response_data = ReadTagSerializer(instance=tag_object).data
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# simple api view
class ListTagV1(APIView):
    
    def get(self, request):
        queryset = Tag.objects.all()
        response_data = ReadTagSerializer(queryset, many=Tag).data 
        return Response(response_data, status=status.HTTP_200_OK)
        
# list api view
class ListTagV2(ListAPIView):
    queryset = Tag.objects.all()
    # _class means a single class 
    serializer_class = ReadTagSerializer
    # _class means a single class 
    pagination_class = StandardResultsSetPagination
    # _classes it means multiple classes / tuple of classes
    throttle_classes = (CustomThrottle, )
    # filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name',]
    ordering_fields = ['created_at']
    filterset_fields = ['id']
    
class TagDetailV1(APIView):
    
    def get(self, request, slug):
        cache_key = f"tag-{slug}"
        if cache.get(cache_key) is not None:
            print("second time, third time, fourth time fetch from cache do not hit database")
            cached_data = cache.get(cache_key)
            return Response(cached_data)
        try:
            tag_object = Tag.objects.get(slug=slug)
        except Tag.DoesNotExist:
            error_response = {"error" : True, "message": "Tag does not exist"}
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
        except Tag.MultipleObjectsReturned:
            error_response = {"error" : True, "message": "Multiple tags exist with the same slug"}
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
        response_data = ReadTagSerializer(instance=tag_object).data 
        print("first time db hit is done and setting up the cache")
        cache.set(cache_key, response_data)
        return Response(response_data, status=status.HTTP_200_OK)
    
class TagDetailV2(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = ReadTagSerializer
    lookup_field = "slug"