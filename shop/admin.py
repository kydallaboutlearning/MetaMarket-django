from django.contrib import admin
from .models import Category,Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    
    #prepolulated fields help automatically gives values which is slug in this case
    prepopulated_fields ={'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Adding List Display"""

    #list_display helps show which the model fields show in the admin fields 
    list_display = ('name',
                     'category',
                     'slug', 
                     'price',
                     'description',
                     'image',
                     'available', 
                     'created',
                     'updated',
                     )
    
    """Adding editable list to be easily edited in the admin interface"""
    list_editable = (
        'price',
        'available',
    )

    """" Adding list filter to filter fields in the admin interface for easy search"""
    list_filter = (
        'category',
        'available',
        'created',
        'updated',
        )
    
    #adding prepolutated fields

    prepopulated_fields =  {'slug': ('name',)}

