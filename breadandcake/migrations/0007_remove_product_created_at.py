# Generated by Django 5.0.2 on 2024-05-30 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breadandcake', '0006_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
    ]
