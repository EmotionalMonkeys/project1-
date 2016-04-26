from django.shortcuts import render
from .forms import CategoryForm
def category(request):
   return render(request, 'project1/category.html',{})
def category_new(request):
   form = CategoryForm()
   return render(request, 'project1/category_edit.html',{'form':form})
