from rest_framework import serializers
from tags.models import Tag

# write operation
class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
  
# read operation
class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'created_at',)
        
