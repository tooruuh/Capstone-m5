# Generated by Django 4.1.1 on 2022-09-09 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
    ]
