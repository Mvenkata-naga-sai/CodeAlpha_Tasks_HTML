from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def home(request):
 return render(request,'home.html',{'posts':Post.objects.all()})

def create_post(request):
 if request.method=='POST':
  Post.objects.create(user=request.user,content=request.POST['content'])
 return redirect('/')

def like(request,id):
 Like.objects.get_or_create(user=request.user,post=Post.objects.get(id=id))
 return redirect('/')

def comment(request,id):
 if request.method=='POST':
  Comment.objects.create(user=request.user,post=Post.objects.get(id=id),text=request.POST['text'])
 return redirect('/')

def register(request):
 if request.method=='POST':
  User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
  return redirect('/login/')
 return render(request,'register.html')

def login_view(request):
 if request.method=='POST':
  user=authenticate(username=request.POST['username'],password=request.POST['password'])
  if user: login(request,user); return redirect('/')
 return render(request,'login.html')

def logout_view(request):
 logout(request); return redirect('/login/')
