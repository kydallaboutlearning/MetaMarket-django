from django.urls import path
from .views import *
from .webhooks import  *

#importing gettextlazy for url translation
from django.utils.translation import gettext_lazy as _



#defining the url patterns

#adding app name
app_name = 'payment'


urlpatterns = [
    path(_('process/'),payment_process, name = 'process'),
    path(_('complete/'),payment_completed, name = 'completed'),
    path(_('cancel/'),payment_cancel, name = 'cancel'),
]