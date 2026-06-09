from django.shortcuts import render,redirect
from .models import Product,Order,OrderItem
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def home(request):
    return render(request,'home.html',{'products':Product.objects.all()})

def product_detail(request,id):
    return render(request,'product.html',{'product':Product.objects.get(id=id)})

def add_to_cart(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    product=Product.objects.get(id=id)
    order,_=Order.objects.get_or_create(user=request.user)
    item,_=OrderItem.objects.get_or_create(order=order,product=product)
    item.quantity+=1
    item.save()
    return redirect('cart')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    order=Order.objects.get(user=request.user)
    items=OrderItem.objects.filter(order=order)
    return render(request,'cart.html',{'items':items})

def register(request):
    if request.method=="POST":
        User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
        return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if request.method=="POST":
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
