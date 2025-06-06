# Generated by Django 5.1.7 on 2025-04-19 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='category',
        ),
        migrations.AddField(
            model_name='inventory',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.subcategory'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.brand'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='unit_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=5, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
