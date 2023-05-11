# Generated by Django 4.1.7 on 2023-04-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("caste", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="pictures")),
                ("desc", models.TextField()),
                ("author", models.CharField(max_length=90)),
                ("date", models.DateField()),
            ],
        ),
    ]
