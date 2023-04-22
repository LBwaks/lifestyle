# Generated by Django 4.1.7 on 2023-04-21 08:44

import Blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0018_alter_profile_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile",
            field=models.ImageField(
                blank=True,
                default="profiles/default_profile.png",
                null=True,
                upload_to="profiles",
                validators=[Blog.validators.validate_file_size],
                verbose_name="Profile Picture",
            ),
        ),
    ]
