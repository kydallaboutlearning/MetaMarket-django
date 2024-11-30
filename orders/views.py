from django.shortcuts import render,redirect,get_object_or_404
import weasyprint
from cart.cart import Cart
from .models import OrderItem, Order
#importing messages
from django.contrib import messages
#importing requirements for the custom admin view
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.staticfiles import finders
from django.http import HttpResponse


#importing requirements for weasyprint
from .forms import OrderCreateform
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

#importing tasks for asynchronous functions
from .tasks import send_order_email

# Create your views here.

def CreateOrderView(request):

    #getting the Existing cart
    cart = Cart(request)
    form = OrderCreateform()

    
    
    #creating a method to handle post request
    if request.method == 'POST':

            #getting if order info is saved before
        create_order_form = OrderCreateform(request.POST)

        if create_order_form.is_valid():
                #saving the order
                order = create_order_form.save(commit = False)
                #checking if the cart has coupom
                if cart.coupon:
                     #saving the order coupon from the cart coupon
                     order.coupon = cart.coupon
                     #saving the discount also
                     order.discount = cart.coupon.discount
                    #saving the order after 
                order.save()
                data = create_order_form.cleaned_data
                name = data['first_name']

                #create an instance of the item in the cart to save in the database
                for item in cart:
                    OrderItem.objects.create(
                        order = order,
                        product = item['product'],
                        price = item['price'],
                        quantity = item['quantity']
                        )
                    
                #adding message
                messages.success(
                     request,'Your Order was successful'
                )    
                
                #deleting the cart
                cart.clear()

               

                

                #adding the payment
                #setting the order session
                request.session['order_id'] = order.id

                #returning the payment
                return redirect('payment:process')
        else:
            form = OrderCreateform()
            messages.error(
                 request,'There was a error with your form'
            )
    else:
            form = OrderCreateform()

    return render(
        request,
        'orders/create_order.html', 
        {
         'form':form,
         'cart':cart
         },
    )


#creating the order detail view
@staff_member_required
def admin_order_detail(request,order_id):
     #getting the order
     order = get_object_or_404(Order,id = order_id)

     #returning the html template
     return render(request, 'admin/orders/order/detail.html',{'order':order})



@staff_member_required
def admin_order_pdf(request, order_id):
    # Fetch the order by ID
    order = get_object_or_404(Order, id=order_id)
    
    # Render the order to an HTML template
    html = render_to_string('admin/orders/order/pdf.html', {'order': order})
    
    # Prepare the HTTP response with the correct content type
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    
    # Use WeasyPrint to generate the PDF
    weasyprint.HTML(string=html).write_pdf(
        response,
        stylesheets=[weasyprint.CSS(finders.find('css/pdf.css'))]
    )
    
    return response