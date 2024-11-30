from django.urls import path
from .views import couponapply

#adding the urls
app_name = 'coupons'

urlpatterns = [
    path('apply_coupon/',couponapply, name = 'apply')
]