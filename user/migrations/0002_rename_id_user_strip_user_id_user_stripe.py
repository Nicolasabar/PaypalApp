# Generated by Django 4.2.15 on 2024-09-10 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="id_user_strip",
            new_name="id_user_stripe",
        ),
    ]
