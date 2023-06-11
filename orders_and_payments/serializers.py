from rest_framework import serializers
from authentication.models import User
from orders_and_payments.models import Order, OrderItems

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email') 


class ReadOrderItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItems
        fields = '__all__' 

class ReadOrderDetailsSerializer(serializers.ModelSerializer):
    
    order_items = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ('id', 'payment_status', 'payment_mode', 'payment_amount', 'user', 'order_items', 'created_at')
        
    def get_order_items(self, order_object):
        qs = order_object.order_items.all()
        return ReadOrderItemsSerializer(qs, many=True).data
    
    def get_user(self, order_object):
        return UserSerializer(instance=order_object.user).data
    
    
    
        
