# Generated by Django 4.2.4 on 2023-08-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trip",
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
                ("driver_id", models.IntegerField()),
                ("vehicle_id", models.IntegerField()),
                ("customer_id", models.IntegerField()),
                ("address", models.CharField(blank=True, max_length=50, null=True)),
                ("cargo_tonnage", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "address_type",
                    models.CharField(
                        choices=[
                            ("pickup_point", "Pickup point"),
                            ("drop_off_point", "Drop off point"),
                        ],
                        default="pickup_point",
                        max_length=20,
                    ),
                ),
                ("done_by_user_id", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Trip",
                "verbose_name_plural": "Trips",
            },
        ),
    ]
