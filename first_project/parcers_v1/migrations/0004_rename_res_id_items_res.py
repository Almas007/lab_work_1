# Generated by Django 4.2 on 2023-04-26 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("parcers_v1", "0003_alter_items_nd_date_alter_items_not_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="items",
            old_name="res_id",
            new_name="res",
        ),
    ]
