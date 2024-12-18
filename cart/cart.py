#importing required modules
from decimal import Decimal
from django.conf import settings
from shop.models import Product
from coupons.models import Coupon

#creating a cart class
class Cart:
    def __init__(self,request):
        """
        initializing cart session
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        #stooring the coupon session
        self.coupon_id = self.session.get('coupon_id')

    def add(self,product,quantity = 1,override_quantity = False):
        """
        adding a product or updating it's quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price' : str(product.price)
            }

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    #creating a save method
    def save(self):
         # mark the session as "modified" to make sure it gets saved
         self.session.modified = True

    #adding remove method 
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    #creating an iteration method
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        #getting the products from the database

        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item  

    #creating method to count products
    def __len__(self):
        """
        counting all items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(
                Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        """
        method for deleting session 
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None
    
    #adding a function to get discount

    def get_discount(self):
        if self.coupon:
            return (
                self.coupon.discount/Decimal(100)
                ) * self.get_total_price()
        return Decimal(0)
    
    #adding a function to get price after discount
    def get_total_price_after_discount(self):
        
        print('getting total price after discount')
        
        return  self.get_total_price() - self.get_discount()

        
 



