# Generated by Django 5.1.1 on 2024-11-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_orderitems_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
