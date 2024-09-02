# Generated by Django 4.2.14 on 2024-08-06 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("items_json", models.CharField(max_length=5000)),
                ("name", models.CharField(max_length=90)),
                ("email", models.CharField(max_length=111)),
                ("address", models.CharField(max_length=111)),
                ("city", models.CharField(max_length=111)),
                ("state", models.CharField(max_length=111)),
                ("pincode", models.CharField(max_length=111)),
            ],
        ),
    ]
