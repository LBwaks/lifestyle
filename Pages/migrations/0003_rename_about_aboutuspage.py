# Generated by Django 4.1.7 on 2023-03-17 05:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Pages", "0002_about_created"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="About",
            new_name="AboutUsPage",
        ),
    ]
