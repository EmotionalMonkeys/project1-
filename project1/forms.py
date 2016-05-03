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


