#importing requirements
from django.urls import path
from . import views


#importing gettextlazy to enable url translation
from django.utils.translation import gettext_lazy as _


app_name = 'shop'

urlpatterns = [
    path('',views.product_list,name = 'product_list'),
    path(_('<slug:category_slug>'),views.product_list,name = 'product_list_by_category'),
    path(_('<int:id>/<slug:slug>/'),views.product_details,name = 'product_detail'),
]
