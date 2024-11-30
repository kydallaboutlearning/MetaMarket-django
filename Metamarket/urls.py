"""
URL configuration for Metamarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/',include('accounts.urls',namespace = 'accounts')),
    # path('buyers/',include('buyers.urls', namespace = 'buyers')),
    # path('sellers',include('sellers.urls',namespace = 'sellers')),
    path('cart/',include('cart.urls',namespace = 'cart')),
    path('payment/',include('payment.urls',namespace = 'payment')),
    path('orders/',include('orders.urls',namespace ='orders')),
    path('coupon/', include('coupons.urls',namespace = 'coupons')),
    path('admin/', admin.site.urls),
    path('__debug__/',include('debug_toolbar.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('',include('shop.urls', namespace = 'shop')),

    ]

if settings.DEBUG:
    urlpatterns += static(
 settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
 )


#customizing the admin site
admin.site.site_header = "Metamarket Admin Portal"
admin.site.site_header = 'MetaMarket'
admin.site.site_title = 'MetaMarket'