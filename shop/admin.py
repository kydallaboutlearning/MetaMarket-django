from django.contrib import admin
from .models import Category,Product
#importing parler to add translatable admin
from parler.admin import TranslatableAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'slug')
    
    #prepolulated fields help automatically gives values which is slug in this case
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
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
    def get_prepopulated_fields(self, request, obj = None):
        return  {'slug': ('name',)}

