# Generated by Django 4.1.1 on 2022-09-20 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("adv", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="adv",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
