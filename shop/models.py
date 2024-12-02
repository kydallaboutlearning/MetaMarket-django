"""Importing requirements"""
from django.db import models
from django.urls import reverse

#importing Parler
from parler.models import TranslatableModel, TranslatedFields

from django.utils.translation import gettext_lazy as _



"""Creating your models here"""
class Category(TranslatableModel):

    #registering the models
    translations = TranslatedFields(
    name = models.CharField(max_length=200),
    slug = models.SlugField(max_length=200,unique=True),
    )

    #creating meta class to help properly identify
    class Meta:
        #remember ordering in parler is impossible due to how parler store related database(laanguages)
        # ordering = ['name']
        # indexes = [models.Index(fields=['name']),]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    #getting absolute url 
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(TranslatableModel):

    #adding the translatable fields
    translations  = TranslatedFields(
    name = models.CharField(max_length = 200),
    slug = models.SlugField(max_length = 200, 
                            unique = True),
    description = models.TextField(blank = True),
    )
    category = models.ForeignKey(Category, 
                                 related_name = 'products',
                                 on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', 
                              blank = True)
    amount_available = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    #creating a functions to set up the availablility
    def check_availability(self):
        if self.Product.amount_available <= 0:
            self.Product.available = False
    
    def __str__(self):
        # Use safe fallback if no translation is available
        return self.safe_translation_getter('name', default=_("Unnamed product"))
    
    #adding an order
    class Meta:

        #removing the ordering of the models
        # ordering = ['name']
         indexes = [#models.Index(fields = ['id','slug']),
        #           models.Index(fields = ['name']),
                   models.Index(fields = ['-created']),
                   ]

    def __str__(self):
        return self.name
    
    #getting absolute url
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
        

    
