from collections import UserDict, UserList
from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to='images',null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    product_image=models.ImageField(upload_to='images',null=False,blank=False)
    description=models.CharField(max_length=300,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(max_length=50,null=False,blank=False)
    selling_price=models.FloatField(max_length=50,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")

    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use the correct User model
    id = models.AutoField(primary_key=True)
    

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart"