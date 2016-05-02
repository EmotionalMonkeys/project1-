from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm,UserForm,ProductForm
from .models import User,Product,Order_shopping,Category

def homepage(request):
	return render(request, 'project1/homepage.html',{})


def user(request):
	form = UserForm()
	return HttpResponse("in user")

def product(request):
	products = Product.objects.order_by('name')
	return render(request, 'project1/product.html', {'products':products})

def product_new(request):
	# if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = ProductForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
      	form.save()
      	return redirect('product')
      #else: Place to raise warning

   # if a GET (or any other method) we'll create a blank form
   else:
      form = ProductForm()

   return render(request, 'project1/product_edit.html', {'form':form})

def product_edit(request,pk):
   product = get_object_or_404(Product, pk=pk)

   if request.method == "POST": #Back with form data
      form = ProductForm(request.POST, instance=product) 
      if form.is_valid():
         form.save()
         return redirect('product')

   else: #Access page 1st time => blank form
      form = ProductForm(instance=product)

   return render(request, 'project1/product_edit.html',{'form':form})
   


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

   return render(request,'project1/category_edit.html',{'form':form})

      #return render(request, 'project1/product_edit.html', {'form':form})
      #return render(request, 'project1/category_edit.html',{'form':form})


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
   
