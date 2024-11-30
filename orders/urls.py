#importing requirements
from django.urls import path
from .views import CreateOrderView,admin_order_detail, admin_order_pdf

#importing gettext_lazy for url translation
from django.utils.translation import gettext_lazy as _



app_name = 'orders'

urlpatterns = [
    path(_('order_create/'),CreateOrderView, name = 'create_order'),
    path(_('admin/orders/<int:order_id>'),admin_order_detail, name = 'admin_order_detail'),
    path(_('admin/orders/<int:order_id>/pdf/'),admin_order_pdf,name = 'admin_order_pdf')
]