# Generated by Django 5.1.3 on 2024-11-28 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Product",
            new_name="ProductModel",
        ),
    ]
