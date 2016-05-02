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
   state = models.CharField(max_length=100)

   def __str__(self):
      return self.username

   def isSeller(self):
      return self.role == 'S'

class Category(models.Model):
    name = models.CharField(max_length=80, null=False, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

    def canDelete(self):
      product = Product.objects.all()
      for p in product:
        if p.category_id == self.id:
         return False

      return True

class Product(models.Model):
   name = models.CharField(max_length=30)
   sku = models.IntegerField(unique=True, null=False)
   price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
   category = models.ForeignKey(Category)
   def __str__(self):
      return self.name
      # + str(self.sku)


class Order_shopping(models.Model):
   customer = models.ForeignKey(User,on_delete=models.CASCADE)
   oSku = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.IntegerField(validators=[MinValueValidator(0)])
   is_bought = models.BooleanField(default=False)
   def __str__(self):
      return self.customer + self.oSku 




   
