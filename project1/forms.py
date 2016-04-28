from django import forms

from .models import User,Category,Product,Order_shopping

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'age','role')



class CategoryForm(forms.ModelForm):   
	class Meta:
		model = Category
		fields = ('name', 'description',)