from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileadmin(admin.ModelAdmin):
    #adding list_display
    list_display = [
        'user',
        'phone_number',
        'created',
        'is_seller',
        'last_login',
    ]

    #adding list_filter
    list_filter =[
        'is_seller',
        'created',
    ]
    raw_id_fields = ['user']