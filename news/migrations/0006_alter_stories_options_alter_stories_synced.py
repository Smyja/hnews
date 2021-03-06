# Generated by Django 4.0.4 on 2022-05-12 20:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0005_alter_stories_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="stories",
            options={},
        ),
        migrations.AlterField(
            model_name="stories",
            name="synced",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
