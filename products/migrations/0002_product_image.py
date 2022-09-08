# Generated by Django 4.1.1 on 2022-09-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default=None,
                height_field=400,
                max_length=250,
                upload_to=None,
                width_field=600,
            ),
        ),
    ]