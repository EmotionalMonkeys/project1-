from django.shortcuts import render
from .forms import CategoryForm
def category(request):
   return render(request, 'project1/category.html',{})

def category_new(request):
   if request.method == "POST": #Back with form data
      form = CategoryForm(request.POST) 
      if form.is_valid():
         category = form.save()
         category.save()

   else: #Access page 1st time => blank form
      form = CategoryForm()

   return render(request, 'project1/category_edit.html',{'form':form})
