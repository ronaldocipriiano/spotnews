# Generated by Django 4.2.3 on 2024-04-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_user_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(),
        ),
    ]
