from rest_framework import serializers
from tags.serializers import ReadTagSerializer
from products.models import Product

# write operation
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'tags')
        
# read operation
class ReadProductSerializer(serializers.ModelSerializer):
    
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'slug', 'created_at', 'price', 'quantity', 'tags')
    
    def get_tags(self, product_object):
        tags = product_object.tags.all()
        serializer_data = ReadTagSerializer(tags, many=True).data 
        return serializer_data
    
        
