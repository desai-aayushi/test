# Generated by Django 4.2.11 on 2024-03-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lostfoundapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="missingitem",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="missing_items_photos/"
            ),
        ),
    ]