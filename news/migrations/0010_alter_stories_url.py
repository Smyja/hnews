# Generated by Django 3.2.13 on 2022-05-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_stories_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='url',
            field=models.URLField(default='', max_length=1000, null=True, verbose_name='URL'),
        ),
    ]
