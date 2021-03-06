from django import forms

from .models import EMUser,Category,Product,Order_shopping

class CategoryForm(forms.ModelForm):   
	class Meta:
		model = Category
		fields = ('name', 'description')
		
class UserForm(forms.ModelForm):
	class Meta:
		model = EMUser
		fields = ('username','age','role', 'state')

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'sku', 'price', 'category')

class OrderShoppingForm(forms.ModelForm):
	class Meta:
		model = Order_shopping
		fields = ('customer', 'oSku', 'quantity', 'is_bought')


class ProductQuantityForm(forms.ModelForm):
	class Meta:
		model = Order_shopping
		exclude = ['customer','oSku','is_bought','purchased_time']

