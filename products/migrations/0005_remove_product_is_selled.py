# Generated by Django 4.1.1 on 2022-09-12 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_product_image_alter_product_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="is_selled",
        ),
    ]
