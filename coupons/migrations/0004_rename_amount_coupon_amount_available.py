# Generated by Django 5.1.1 on 2024-11-26 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_coupon_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='amount',
            new_name='amount_available',
        ),
    ]
