# Generated by Django 4.1 on 2024-07-05 08:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Musician",
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
                ("first_name", models.CharField(max_length=63)),
                ("last_name", models.CharField(max_length=63)),
                ("instrument", models.CharField(max_length=63)),
                (
                    "age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                14, message="You must be 14 years old or older"
                            )
                        ]
                    ),
                ),
                ("date_of_applying", models.DateField(auto_now=True)),
            ],
        ),
    ]
