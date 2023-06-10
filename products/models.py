from django.db import models
from tags.models import Tag

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.BigIntegerField(default=0)
    quantity = models.BigIntegerField(default=0)
