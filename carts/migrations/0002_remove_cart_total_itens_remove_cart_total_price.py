# Generated by Django 4.1.1 on 2022-09-09 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="total_itens",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="total_price",
        ),
    ]
