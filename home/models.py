from cProfile import label
from email.mime import image
from django.db import models

# Create your models here.
#Model for Slider
STATUS = (('active','Active'),('','Default'))
class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media')#upload Image code
    topic = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    price = models.FloatField(blank=True)
    rank = models.IntegerField()
    status = models.CharField(choices= STATUS,blank=True,max_length=100)

    def __str__ (self):
        return self.name

class PopupNewsletter(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media')
    discount_per = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__ (self):
        return self.discount_per


#Model for Ads
class AdsBanner(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media')
    label = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    BannerRank = models.IntegerField()
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media')
    
    def __str__(self):
        return self.name

# Model for Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    slug = models.TextField(unique = True)

    def __str__(self):
        return self.name

#Model for Subcategory of Category
class SubCategory(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    icon = models.CharField(max_length=200,blank=True)
    slug = models.TextField(unique = True)


#for product
LABELS = (('dealDay','DealDay'),('new','New'),('hot','Hot'),('sale','Sale'),('','default'))
STOCK = (('In Stock','In Stock'),('Out Stock','Out Stock'))
class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField()
    discount_price = models.FloatField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to = 'media')#upload Image code
    image2 = models.ImageField(upload_to = 'media')#upload Image code
    image3 = models.ImageField(upload_to = 'media',null=True)#upload Image code
    image4 = models.ImageField(upload_to = 'media',null=True)#upload Image code
    brief_Description = models.TextField(blank = True)
    description = models.TextField(blank = True)
    specification = models.TextField(blank=True)
    shipping = models.TextField(blank=True)
    slug = models.TextField(unique = True)
    labels = models.CharField(choices= LABELS,max_length=100)
    stock = models.CharField(choices= STOCK,max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400)
    Reaction = models.CharField(max_length=400)
    Review = models.TextField(blank=True)
    slug = models.TextField()
    date = models.CharField(max_length=400)
    point = models.IntegerField(default=1)

    def __str__(self):
        return self.name
