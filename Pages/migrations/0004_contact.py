# Generated by Django 4.1.7 on 2023-03-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Pages", "0003_rename_about_aboutuspage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("message", models.CharField(max_length=50, verbose_name="Message")),
                ("content", models.TextField(verbose_name="Description")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
            },
        ),
    ]