# Generated by Django 4.1.7 on 2023-04-03 08:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0011_alter_profile_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="profile",
        ),
    ]