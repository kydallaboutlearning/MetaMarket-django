"""Importing required Items"""
from django import forms
from .models import Order, OrderItem


""""Creating a model form from Order models"""

class OrderCreateform(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'postal_code',
            'address',
            'city'
            ]
        
        
        
    