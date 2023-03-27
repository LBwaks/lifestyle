# Generated by Django 4.1.7 on 2023-03-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Pages", "0004_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="content",
        ),
        migrations.AddField(
            model_name="contact",
            name="subject",
            field=models.CharField(
                default="now", max_length=50, verbose_name="Subject"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(verbose_name="Description"),
        ),
    ]
