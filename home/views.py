from email.mime import base
from urllib import request
from django.shortcuts import render
from django.views import View
from .models import *


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