# Generated by Django 4.1.7 on 2023-04-01 18:04

import Blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0007_alter_profile_facebook_alter_profile_instagram_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="profiles",
                validators=[Blog.validators.validate_file_size],
                verbose_name="Profile Picture",
            ),
        ),
    ]
