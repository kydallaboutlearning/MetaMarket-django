import stripe
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
import logging
from orders.tasks import payment_completed_email
from shop.recommender import  Recommender
from shop.models import Product



# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def stripe_webhook(request):
    # Retrieve the request body and signature
    payload = request.body
    signature = request.META.get('HTTP_STRIPE_SIGNATURE', None)
    if signature is None:
        logger.error("Missing Stripe signature")
        return HttpResponse(status=400)

    try:
        event = stripe.Webhook.construct_event(payload, signature, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        # Invalid payload
        logger.error("Invalid payload: %s", e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.error("Invalid signature: %s", e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                # Get the order
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                # Order does not exist
                logger.error("Order with ID %s not found", session.client_reference_id)
                return HttpResponse(status=404)

            # Mark the order as paid
            order.paid = True
            order.stripe_id = session.payment_intent
            order.save()

            #saving the other producst bought using recommender
            product_ids = order.items.values_list('product_id'
                                                  )
            products = Order.objects.filter(id__in = product_ids)
            r = Recommender()
            r.products_bought(products)
            print('recommmender')
            
            # Send a signal to the task queue to update the order status
            payment_completed_email.delay(order.id)

            logger.info("Order %s marked as paid", order.id)
            return HttpResponse(status=200)

    else:
        # Log unhandled events
        logger.warning("Unhandled event type: %s", event.type)
        return HttpResponse(status=400)

    return HttpResponse(status=200)