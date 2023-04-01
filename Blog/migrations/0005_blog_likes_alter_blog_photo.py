# Generated by Django 4.1.7 on 2023-04-01 18:04

import Blog.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Blog", "0004_blog_bookmarks"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blogs",
                validators=[Blog.validators.validate_file_size],
                verbose_name="Photo",
            ),
        ),
    ]
