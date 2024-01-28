from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/products')
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    condition= models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    shipping = models.TextField()
    availability = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/categories' , blank=True, null=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    
   
    def __str__(self):
        return self.user.username + " - " + self.product.name
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    estimated_date_of_arrival = models.CharField(max_length= 20 , blank=True, null=True)
    viewed = models.BooleanField(blank=True, null=True , default=False)
    received = models.BooleanField(blank=True, null=True, default=False)
   
    def __str__(self):
        return self.user.username + " - " + self.product.name
    
# class ReceivedItem(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     product = models.ForeignKey('Product',on_delete=models.CASCADE)
#     received_date = models.CharField(max_length= 20 , blank=True, null=True)

#     def __str__(self):
#         return self.user.username + " received " + self.product.name
    
class Profile(models.Model):
    image = models.ImageField(upload_to='images/profiles' , blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=20)
   
    def __str__(self):
        return self.user.username
   
