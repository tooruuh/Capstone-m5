# Generated by Django 4.1.1 on 2022-09-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="", max_length=50),
        ),
    ]
