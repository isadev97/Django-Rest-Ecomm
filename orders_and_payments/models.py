from django.db import models
from authentication.models import User
from django.utils.translation import gettext_lazy as _
from products.models import Product
from model_utils import Choices

# Create your models here.
class Order(models.Model):
    PAYMENT_MODES = Choices(
        (1, "cod", _("cod")), # cash on delivery
        (2, "card", _("card")),
        (3, "upi", _("upi")),
        (4, "netbanking", _("netbanking")),
    )
    PAYMENT_STATUS = Choices(
        (1, "completed", _("completed")), 
        (2, "pending", _("pending")),
    )
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    payment_mode = models.IntegerField(choices=PAYMENT_MODES, default=PAYMENT_MODES.cod)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS, default=PAYMENT_STATUS.pending)
    payment_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_at_the_time_of_order = models.IntegerField(default=0)
    price_at_the_time_of_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    


    