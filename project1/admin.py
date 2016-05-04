from django.contrib import admin
from .models import EMUser,Category,Product,Order_shopping
# Register your models here.
admin.site.register(EMUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order_shopping)
