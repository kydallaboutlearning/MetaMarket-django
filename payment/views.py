from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from orders.models import Order
from django.http import HttpResponse
import stripe
from decimal import Decimal


# Getting the stripe Data from settings
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION    
stripe.webhook_secret = settings.STRIPE_WEBHOOK_SECRET

# Create your views here.
def payment_process(request):

    #saving the order id to send out data from database to stripe
    order_id = request.session['order_id']
    order = get_object_or_404(Order,id=order_id)

    #getting from poost data
    if request.method == 'POST':
        #creating the success url
        success_url = request.build_absolute_uri(reverse("payment:completed"))

        #creatiing the cancel url
        cancel_url = request.build_absolute_uri(reverse('payment:cancel'))

        #getting the session data for stripe to use
        session_data = {
            'mode':'payment',
            'client_reference_id':order_id,
            'line_items':[],
            'success_url':success_url,
            'cancel_url':cancel_url,
           
        }

        #adding data to session_data

        for item in order.items.all():
            session_data['line_items'].append(
                {
                    'price_data': {
                        'unit_amount': int(item.price * Decimal('100')),
                        'currency': 'usd',
                        'product_data': {
                            'name': item.product.name,
                        },
                    },
                    'quantity': item.quantity,
                }
            )

        # Stripe coupon
        if order.coupon:
            stripe_coupon = stripe.Coupon.create(
                name=order.coupon.code,
                percent_off=order.discount,
                duration='once',
            )
            session_data['discounts'] = [{'coupon': stripe_coupon.id}]
        print(session_data)
        # create Stripe checkout session
        session = stripe.checkout.Session.create(**session_data)


        #returning the url after the checkout 


        return redirect(session.url, code=303)
    else:
        return render(request,'payment/process.html',locals())
    

#adding payment success view
def payment_completed(request):
    return render(request,'payment/completed.html')

#adding payment cancel

def payment_cancel(request):
    return render(request,'payment/cancel.html')



