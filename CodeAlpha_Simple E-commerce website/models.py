from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.URLField()
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
