# Generated by Django 5.1.7 on 2025-05-01 12:48

import django.db.models.deletion
import payment.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0013_remove_profile_address_remove_profile_phone_number'),
        ('order', '0004_remove_orderline_inventory_orderline_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('cod', 'Cash on Delivery'), ('gcash', 'GCash'), ('paypal', 'PayPal')], default='cod', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=payment.models.payments_image_path)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
