# Generated by Django 5.0 on 2024-03-26 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_seller_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller_Order',
            fields=[
                ('seller_order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=50, null=True)),
                ('user_id', models.BigIntegerField()),
                ('shipping_address', models.CharField(max_length=200, null=True)),
                ('total_value', models.IntegerField(default=0, null=True)),
                ('payment_method', models.CharField(max_length=50, null=True)),
                ('seller_id', models.BigIntegerField(null=True)),
            ],
            options={
                'db_table': 'seller_order',
            },
        ),
        migrations.CreateModel(
            name='User_Order',
            fields=[
                ('user_order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=50, null=True)),
                ('user_id', models.BigIntegerField()),
                ('shipping_address', models.CharField(max_length=200, null=True)),
                ('total_value', models.IntegerField(default=0, null=True)),
                ('payment_method', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'user_order',
            },
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='order_id',
        ),
        migrations.CreateModel(
            name='Seller_Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.BigIntegerField()),
                ('amount', models.IntegerField(null=True)),
                ('Seller_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.seller_order')),
            ],
            options={
                'db_table': 'seller_order_item',
            },
        ),
        migrations.CreateModel(
            name='User_Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.BigIntegerField()),
                ('amount', models.IntegerField(null=True)),
                ('user_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.user_order')),
            ],
            options={
                'db_table': 'user_order_item',
            },
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order_item',
        ),
    ]
