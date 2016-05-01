from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm
from .models import Category
def category(request):
   categories = Category.objects.order_by('name')
   return render(request,'project1/category.html',{'categories':categories})

def category_new(request):
   if request.method == "POST": #Back with form data
      form = CategoryForm(request.POST) 
      if form.is_valid():
         form.save()
         return redirect('category')
   else: #Access page 1st time => blank form
      form = CategoryForm()

   return render(request, 'project1/category_edit.html',{'form':form})

def category_edit(request,pk):
   category = get_object_or_404(Category, pk=pk)
   if request.method == "POST": #Back with form data
      form = CategoryForm(request.POST, instance=category) 
      if form.is_valid():
         form.save()
         return redirect('category')

   else: #Access page 1st time => blank form
      form = CategoryForm(instance=category)

   return render(request, 'project1/category_edit.html',{'form':form})
   

   
