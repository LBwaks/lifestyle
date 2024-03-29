# Generated by Django 4.1.7 on 2023-04-18 07:08

import Blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0016_alter_profile_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile",
            field=models.ImageField(
                blank=True,
                default="static/images/default_profile.png",
                null=True,
                upload_to="profiles",
                validators=[Blog.validators.validate_file_size],
                verbose_name="Profile Picture",
            ),
        ),
    ]
