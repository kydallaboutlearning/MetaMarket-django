from django.urls import path
from .views import couponapply
from django.utils.translation import gettext_lazy as _


#adding the urls
app_name = 'coupons'

urlpatterns = [
    path(_('apply_coupon/'),couponapply, name = 'apply')
]