from django.urls import path
from .views import (cart_detail, 
                   cart_add,
                   cart_remove
                   )

#importing gettext_lazy for translation
from django.utils.translation import gettext_lazy as _

app_name = 'cart'

#adding the paths
urlpatterns = [
    path('', cart_detail, name = 'cart_detail' ),
    path(_('add_to_cart/<int:product_id>/'), cart_add, name ='add_to_cart'),
    path(_('remove/<int:product_id>/'), cart_remove, name = 'remove_cart')
]