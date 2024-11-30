from django.contrib import admin
#importing requirement for setting the stripe payment url
from django.utils.safestring import mark_safe
from django.urls import reverse


#importing requirements for exporting csv files
import csv
import datetime
from django.http import HttpResponse


#importing models
from .models import *


#creating a modelinline admin

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['order',
                     'product',
                     ]
    



# Function to export data to CSV
def export_to_csv(modeladmin, request, queryset):
    # Getting metadata of the model
    opts = modeladmin.model._meta

    # Setting the filename for the CSV file
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'

    # Preparing the HTTP response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition

    # Writing CSV data
    writer = csv.writer(response)

    # Getting fields, excluding many-to-many and one-to-many relationships
    fields = [
        field
        for field in opts.get_fields()
        if not field.many_to_many and not field.one_to_many
    ]

    # Writing header row with field names
    writer.writerow([field.verbose_name for field in fields])

    # Writing data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)

    return response

# Adding a short description for the admin action
export_to_csv.short_description = "Export selected items to CSV"







#creating a decorator to register the models
@admin.register(Order)
#creating an admin class for orders
class OrderAdmin(admin.ModelAdmin):
    #adding the export to csv function to the order admin
    actions = [export_to_csv]

    """Creating a list display to show fields that would display in the admin panel"""
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'address',
        'created',
        'updated',
        'order_detail',
        'order_pdf',
        'city',
        'order_payment',
        'paid',
        ]
    list_filter = [
        'paid',
        'created',
        'updated',
    ]
    inlines = [OrderItemInline]
    #creating a function to generate the payment url for the order
   # Define the order_payment method
    def order_payment(self, obj):
        # Get the Stripe URL for the order
        url = obj.get_stripe_url()

        if obj.stripe_id:
            # Create the clickable HTML link
            html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
            # Mark the HTML as safe to prevent escaping
            return mark_safe(html)

        # Return an empty string if no stripe_id is present
        return ''

    # Set the column name for order_payment in the admin panel
    order_payment.short_description = 'Stripe Payment'


    #creating an order_detail function
    def order_detail(self, obj):
        url = reverse('orders:admin_order_detail', args = [obj.id])
        return mark_safe(f'<a href="{url}">view</a>')
    
    def order_pdf(self,obj):
        url = reverse('orders:admin_order_pdf', args=[obj.id])
        return mark_safe(f'<a href="{url}">PDF</a>')
    order_pdf.short_description = 'Invoice'