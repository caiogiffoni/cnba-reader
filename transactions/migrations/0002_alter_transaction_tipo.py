# Generated by Django 4.1.2 on 2022-10-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="tipo",
            field=models.SmallIntegerField(unique=True),
        ),
    ]
