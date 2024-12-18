from django.db import models
from django.conf import settings
from decimal import Decimal
from coupons.models import Coupon
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _



# Create your models here.

class Order(models.Model):
    first_name =  models.CharField(_('first name'),max_length = 50)
    last_name = models.CharField(_('last name'),max_length = 50)
    email = models.EmailField(_('e-mail')) 
    address = models.CharField(_('address'), max_length = 500)
    postal_code = models.CharField(_('postal code'),max_length = 10)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    city = models.CharField(_('city'), max_length = 100)
    paid = models.BooleanField(default = False )
    coupon = models.ForeignKey(
        Coupon,
        related_name='orders',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,

    )
    discount = models.IntegerField(
                            default = 0,
                            validators=[MinValueValidator,MinValueValidator]
                            )

    
    
    #adding the stripe id
    stripe_id = models.CharField(max_length = 300, blank = True, null = True)
    """ Adding metadata for proper placing"""
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields = ['created']),]

    def __str__(self):
        return f'order {self.id}'
    
    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())
        
    
    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return self.discount/Decimal(100) * total_cost
        
        return Decimal(0)

    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()
    
    def get_stripe_url(self):
        if not self.stripe_id:
            #no payment has been made
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:
            #test mode is on
            path = 'test/'
        else:
            #test mode is off
            path = '/'
        #creating the stripe url
        return f'https://dashboard.stripe.com/payments/{path}{self.stripe_id}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items' , on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', related_name='order_items', on_delete = models.CASCADE)
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    




