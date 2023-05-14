from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import CreateTagSerializer, ReadTagSerializer
from tags.models import Tag
from rest_framework import status
from django.utils.text import slugify

class CreateTag(APIView):

    def post(self, request):
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
            return Response(response_data,status=status.HTTP_200_OK)
        else:
            return Response(create_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    