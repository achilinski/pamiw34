# Generated by Django 4.2.6 on 2023-11-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_book_date_of_publishing"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="rating",
            field=models.FloatField(default=0),
        ),
    ]