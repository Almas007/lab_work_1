# Generated by Django 4.2 on 2023-04-26 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("parcers_v1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Items",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.CharField(max_length=255)),
                ("title", models.TextField()),
                ("content", models.TextField()),
                ("nd_date", models.DateField()),
                ("s_date", models.DateField()),
                ("not_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("resource_name", models.CharField(max_length=255)),
                ("resource_url", models.CharField(max_length=255)),
                ("top_tag", models.CharField(max_length=255)),
                ("bottom_tag", models.CharField(max_length=255)),
                ("title_cut", models.CharField(max_length=255)),
                ("date_cut", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="Parcer",
        ),
        migrations.AddField(
            model_name="items",
            name="res_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="resource_id",
                to="parcers_v1.resource",
            ),
        ),
    ]
