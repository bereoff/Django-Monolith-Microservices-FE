# Generated by Django 5.0.2 on 2024-02-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-date_posted"],
            },
        ),
    ]