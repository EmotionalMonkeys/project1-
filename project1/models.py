from django.db import models
from django.core.validators import MinValueValidator
# User 
class User(models.Model):
   username = models.CharField(max_length=50,primary_key=True)
   age = models.IntegerField(validators=[MinValueValidator(0)])
   role_avail = (
      ('S', 'Seller'),
      ('B', 'Buyer'),
   )
   role = models.CharField(max_length=1, choices=role_avail)
   def __str__(self):
      return self.username

class Category(models.Model):
    name = models.CharField(max_length=80, null=False, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name + self.description

class Product(models.Model):
   name = models.CharField(max_length=30)
   sku = models.UUIDField(primary_key=True)
   price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
   category = models.ForeignKey(Category)
   def __str__(self):
      return self.name + self.sku


class Order_shopping(models.Model):
   customer = models.ForeignKey(User,on_delete=models.CASCADE)
   oSku = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.IntegerField(validators=[MinValueValidator(0)])
   is_bought = models.BooleanField(default=False)
   def __str__(self):
      return self.customer + self.oSku 




   
