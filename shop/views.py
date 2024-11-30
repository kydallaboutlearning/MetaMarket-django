from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from cart.forms import CartAddProductForm
from cart.cart import *

from cart.cart import Cart

#import the recommender to help show recommended products
from .recommender import Recommender

#importing decorators for Enabling Login
from django.contrib.auth.decorators import login_required

# Create your views here.

"""Creating the views """

#adding the decorator
#remember to add login required when you add the landing page
def product_list(request,category_slug = None):
    category =  None
    cart = Cart(request)
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category = category)
    return render(request,'shop/product/list.html',
                  {'category':category,
                  'categories':categories,
                  'products': products,
                  'cart': cart,
                  }
                  )


def product_details(request,id,slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    r = Recommender()
    recommended_products = r.suggest_products_for([product] ,4)
    return render(request,'shop/product/detail.html',
                  {'product':product,
                   'cart_product_form':cart_product_form,
                  'recommended_products':recommended_products,
                  'cart': cart,
                  }
                  )