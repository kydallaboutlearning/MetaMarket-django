"""Importing requirements"""
from django.db import models
from django.urls import reverse



"""Creating your models here"""
class Category(models.Model):

    #registering the models
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)

    #creating meta class to help properly identify
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    #getting absolute url 
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'products', on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique = True)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True)
    amount_available = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    #creating a functions to set up the availablility
    def check_availability(self):
        if self.Product.amount_available <= 0:
            self.Product.available = False
    
    #adding an order
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields = ['id','slug']),
                   models.Index(fields = ['name']),
                   models.Index(fields = ['-created']),
                   ]

    def __str__(self):
        return self.name
    
    #getting absolute url
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
        

    
