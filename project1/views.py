from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .forms import CategoryForm,UserForm,ProductForm
from .models import EMUser,Product,Order_shopping,Category
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User

def homepage(request):
	return render(request, 'project1/homepage.html',{'user':request.user.username})

def login(request):
   c = {} #dict
   c.update(csrf(request))
   return render_to_response('project1/login.html',c)

def auth_view(request):
   #If username is empty, fill username with ''
   username = request.POST.get('username')
   user = auth.authenticate(username=username, password = '')
   if user is not None and user.is_active:
      auth.login(request,user)
      return render(request, 'project1/homepage.html',{'user':request.user.username})
   else:
      return render(request, 'project1/login.html',
         {'message1':"The provided name ", 'user':username, 'message2':" is not known."})

def signup(request):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = UserForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
         form.save()
         user = User.objects.create_user(username=request.POST.get('username'))
         user.set_password('')
         user.save()
         return redirect('homepage')
   else:
      form = UserForm()

   return render(request, 'project1/signup.html', {'form':form})

def product(request,pk=None, curCat='All'):
   try:
      user = EMUser.objects.get(username=request.user.username)
   except EMUser.DoesNotExist:
      user = None
   if request.user.is_authenticated():
      if user.role == 'owner':
         if pk != None:
            selectedCategory = get_object_or_404(Category, pk=pk)
            curCat = selectedCategory.name
            products = Product.objects.filter(category_id=selectedCategory)
         else:
            products = Product.objects.order_by('name')
         allCategories = Category.objects.order_by('name')

         return render(request, 'project1/product.html', 
            {'products':products,'allCategories':allCategories,'curCat':curCat})
      else:
         return render(request,'project1/homepage.html',
            {'error':"This page is available to owners only"})
   else:
      return render(request,'project1/homepage.html',{'error':"No user logged in"})

def product_search(request):
   searchItem = request.GET['item']
   curCat = request.GET['curCat']
   selCat = Category.objects.filter(name=curCat)
   if curCat != 'All':
      products = Product.objects.filter(name__contains=searchItem).filter(category=selCat)
   else:
      products = Product.objects.filter(name__contains=searchItem)
   allCategories = Category.objects.order_by('name')
   return render(request, 'project1/product.html', 
                 {'products':products,'allCategories':allCategories , 'curCat':curCat, 'searchItem':searchItem})

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

   else: 
      form = ProductForm(instance=product)

   return render(request, 'project1/product_edit.html',{'form':form})
   

def product_delete(request,pk):
   Product.objects.get(pk=pk).delete()
   messages.success(request, "Successfully deleted")
   return redirect('product')


def category(request):
   user = EMUser.objects.get(username=request.user.username)
   if request.user.is_authenticated():
      if user.role == 'owner':
         categories = Category.objects.order_by('name')
         return render(request,'project1/category.html',{'categories':categories})
      else:
         return render(request,'project1/homepage.html',
            {'error':"This page is available to owners only"})
   else:
      return render(request,'project1/homepage.html',{'error':"No user logged in"})

def categoryAccessError(request):
   messages.error(request, 'Cannot aceess.')
   return redirect('homepage')


def category_new(request):
   if request.method == "POST": #Back with form data
   	form = CategoryForm(request.POST) 
   	if form.is_valid():
         form.save()
         return redirect('category')
   else: #Access page 1st time => blank form
   	form = CategoryForm()

   return render(request,'project1/category_edit.html',{'form':form})

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


def category_delete(request,pk):
   Category.objects.get(pk=pk).delete()
   messages.success(request, "Successfully deleted")
   return redirect('category')

def product_browse(request, pk=None):
   if pk != None:
      selectedCategory = get_object_or_404(Category, pk=pk)
      products = Product.objects.filter(category_id=selectedCategory)
   else:
      products = Product.objects.order_by('name')
   categories = Category.objects.order_by('name')
   return render(request, 'project1/product_browse.html', {'products':products, 'categories':categories})


def product_browse_search(request):
   searchItem = request.GET['item']
   curCat = request.GET['curCat']
   selCat = Category.objects.filter(name=curCat)
   if curCat != 'All':
      products = Product.objects.filter(name__contains=searchItem).filter(category=selCat)
   else:
      products = Product.objects.filter(name__contains=searchItem)
   allCategories = Category.objects.order_by('name')
   return render(request, 'project1/product_browse.html', 
                 {'products':products,'allCategories':allCategories , 'curCat':curCat, 'searchItem':searchItem})

def product_order(request, pk=None):
   quantity = request.POST.get('quantity')
   if quantity is not None:
      quantity.save()
   if pk != None:
      selectedProduct = get_object_or_404(Product, pk = pk)
      #products = Product.objects.filter(selectedProduct)
      return render(request, 'project1/product_order.html', {'selectedProduct':selectedProduct})
   else:
      products = Product.objects.order_by('name')
      categories = Category.objects.order_by('name')
      return render(request, 'project1/product_browse.html', {'products':products, 'categories':categories})

def order_new(request):
   if request.method == "POST": #Back with form data
      form = OrderShoppingForm(request.POST) 
      if form.is_valid():
         form.save()
         return redirect('product_browse')
   else: #Access page 1st time => blank form
      form = OrderShoppingForm()

   return render(request,'project1/product_order_edit.html',{'form':form})

def product_order_edit(request,pk):
   order = get_object_or_404(Order_shopping, pk=pk)

   if request.method == "POST": #Back with form data
      form = OrderShoppingForm(request.POST, instance=order) 
      if form.is_valid():
         form.save()
         return redirect('product_browse')

   else: #Access page 1st time => blank form
      form = OrderShoppingForm(instance=category)

   return render(request, 'project1/product_order_edit.html',{'form':form})

def shopping_cart(request):
   productInCart = Order_shopping.objects.filter(is_bought=False).filter(customer=request.user.username)
   skuToName = []
   quantityToPrice = [] 
   for product in productInCart: 
      quantityToPrice.append(zip(product,skuToName.append(Product.objects.get(sku=product.oSku))))
   return render(request, 'project1/shopping_cart.html', {'quantityToPrice':quantityToPrice})

   #{'productInCart':productInCart,'skuToName':skuToName})
   
