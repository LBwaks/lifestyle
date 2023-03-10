# Generated by Django 4.1.7 on 2023-03-10 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Accounts", "0002_profile_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_profile",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
