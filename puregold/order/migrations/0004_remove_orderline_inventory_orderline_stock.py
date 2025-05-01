import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_alter_brand_name'),
        ('order', '0003_order_alter_orderline_order_delete_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='inventory',
        ),
        migrations.AddField(
            model_name='orderline',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.stock'),
        ),
    ]