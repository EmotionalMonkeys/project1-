from django import forms

from .models import User,Category,Product,Order_shopping

class CategoryForm(forms.ModelForm):   
	class Meta:
		model = Category
		fields = ('name', 'description')
		
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','age','role')

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'sku', 'price', 'category')

