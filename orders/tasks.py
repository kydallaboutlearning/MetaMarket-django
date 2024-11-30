from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from django.core.mail import EmailMessage
from django.contrib.staticfiles import finders
from django.template.loader import render_to_string
from io import BytesIO
import weasyprint


#creating the asynchronous
@shared_task
def send_order_email(order_id):

    #getting order content
    order = Order.objects.get(id=order_id)

    #creating the email content
    subject = f'Order nr.{order_id}'
    message = f"Dear {order.first_name},\n\nYour order has been received.\n\n Thanks for shopping with us."
    mail_sent = send_mail(
        subject,message,"kydallaboutlearning@gmail.com",order.email
        )
    #returning the email
    return mail_sent


@shared_task
def payment_completed_email(order_id):
    """Sending email to users once payment is completed"""
    order = Order.objects.get(id=order_id)
    message = 'Pls find the invoice attached to for your recent purchase'
    subject = f'MetaMarket - Invoice of order nr.{order.id}'
    email = EmailMessage(subject, message, 'kydallaboutlearning@gmail.com', [order.email])

    #generating pdf
    html = render_to_string('admin/orders/order/pdf,html',{'order':order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(finders.find('css/pdf.css'))]
    weasyprint.HTML(string=html).write_pdf(out,styelsheets=stylesheets)
    #attaching the pdf file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    #send the email
    email.send()

