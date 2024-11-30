#importing requirements
from django.urls import path
from .views import CreateOrderView,admin_order_detail, admin_order_pdf

app_name = 'orders'

urlpatterns = [
    path('order_create/',CreateOrderView, name = 'create_order'),
    path('admin/orders/<int:order_id>',admin_order_detail, name = 'admin_order_detail'),
    path('admin/orders/<int:order_id>/pdf/',admin_order_pdf,name = 'admin_order_pdf')
]