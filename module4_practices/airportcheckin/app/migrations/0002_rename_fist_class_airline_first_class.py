# Generated by Django 4.1.5 on 2023-02-11 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="airline",
            old_name="fist_class",
            new_name="first_class",
        ),
    ]
