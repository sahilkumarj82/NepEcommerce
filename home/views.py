import email
import imp
from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View
import datetime
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import login,logout


# Create your views here.

class Base(View):
    views = {}

class HomeView(Base):
    def get(self,request):
        self.views
        self.views['sliders'] = Slider.objects.all() # get all slider and shows
        self.views['popupnews'] = PopupNewsletter.objects.all() # get all slider and shows
        self.views['AdsBanners'] = AdsBanner.objects.all() # get all slider and shows
        self.views['brands'] = Brand.objects.all()
        self.views['dealofdays'] = Product.objects.filter(labels = 'dealDay') # filtering products from labels from models
        self.views['hots'] = Product.objects.filter(labels = 'hot') # filtering products from labels from models
        self.views['sales'] = Product.objects.filter(labels = 'sale') # filtering products from labels from models
        self.views['news'] = Product.objects.filter(labels = 'new') # filtering products from labels from models
        self.views['allProducts']  = Product.objects.all()
        self.views['categories']  = Category.objects.all()
        return render(request,'index-1.html',self.views)

class ProductDetaileView(Base):
    def get(self,request,slug):
        self.views
        self.views['details'] = Product.objects.filter(slug = slug) 
        return render(request,'product.html',self.views)


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:

            if User.objects.filter(username = username).exists(): #check whether user exits or not
                messages.error(request,"The Username is already taken")
                return redirect('/signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request,"The email is already taken")
                return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = f_name,
                    last_name = l_name
                )
                data.save()
                return redirect('/')

        else:
            messages.error(request,"The password does not match")
            return redirect('/signup')

    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.error(request,'The username or password doesnot match')
            return redirect('/login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')