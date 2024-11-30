from django.urls import path
from .views import *
from .webhooks import  *

#defining the url patterns

#adding app name
app_name = 'payment'

urlpatterns = [
    path('process/',payment_process, name = 'process'),
    path('complete/',payment_completed, name = 'completed'),
    path('cancel/',payment_cancel, name = 'cancel'),
    path('webhook/',stripe_webhook, name='stripe-webhook'),
]