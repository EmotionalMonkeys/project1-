from django.db import models
from django.core.validators import MinValueValidator
# User 
class EMUser(models.Model):
   username = models.CharField(max_length=50,unique = True, primary_key=True)
   age = models.IntegerField(validators=[MinValueValidator(0)])
   role_avail = (
      ('owner', 'Owner'),
      ('customer', 'Customer'),
   )

   role = models.CharField(max_length=10, choices=role_avail)

   state_avail = (
      ('AL','Alabama' ),
      ('AK','Alaska' ),
      ('AZ','Arizona' ),
      ('AR','Arkansas' ),
      ('CA','California' ),
      ('CO','Colorado' ),
      ('CT','Connecticut' ),
      ('DE','Delaware' ),
      ('FL','Florida' ),
      ('GA','Georgia' ),
      ('HI','Hawaii' ),
      ('ID','Idaho' ),
      ('IL','Illinois'),
      ('IN','Indiana' ),
      ('IA','Iowa' ),
      ('KS','Kansas' ),
      ('KY','Kentucky' ),
      ('LA','Louisiana' ),
      ('ME','Maine' ),
      ('MD','Maryland' ),
      ('MA','Massachusetts' ),
      ('MI','Michigan' ),
      ('MN','Minnesota' ),
      ('MS','Mississippi' ),
      ('MO','Missouri' ),
      ('MT','Montana' ),
      ('NE','Nebraska' ),
      ('NV','Nevada' ),
      ('NH','New Hampshire' ),
      ('NJ','New Jersey' ),
      ('NM','New Mexico' ),
      ('NY','New York' ),
      ('NC','North Carolina' ),
      ('ND','North Dakota' ),
      ('OH','Ohio' ),
      ('OK','Oklahoma' ),
      ('OR','Oregon' ),
      ('PA','Pennsylvania' ),
      ('RI','Rhode Island' ),
      ('SC','South Carolina' ),
      ('SD','South Dakota' ),
      ('TN','Tennessee' ),
      ('TX','Texas' ),
      ('UT','Utah' ),
      ('VT','Vermont' ),
      ('VA','Virginia' ),
      ('WA','Washington' ),
      ('WV','West Virginia' ),
      ('WI','Wisconsin' ),
      ('WY','Wyoming'),
   )
   state = models.CharField(max_length=2, choices=state_avail)

   def __str__(self):
      return self.username

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
   sku = models.CharField(unique=True, null=False, max_length=10)
   price = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
   category = models.ForeignKey(Category)
   def __str__(self):
      return self.name
   


class Order_shopping(models.Model):
   customer = models.ForeignKey(EMUser,on_delete=models.CASCADE)
   oSku = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.IntegerField(validators=[MinValueValidator(0)])
   is_bought = models.BooleanField(default=False)
   def __str__(self):
      return self.customer + self.oSku 




   
