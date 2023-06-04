from rest_framework import serializers
from tags.models import Tag

# write operation
class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
        

class ExtraFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('updated_at',)
  
# read operation
class ReadTagSerializer(serializers.ModelSerializer):
    
    extra_field = serializers.SerializerMethodField() # works a nested serializer field
    
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'created_at', 'extra_field')
        
    def get_extra_field(self, tag_object):
        serialized_data = ExtraFieldSerializer(instance=tag_object).data
        print("serialized_data", serialized_data)
        return serialized_data
    
        
