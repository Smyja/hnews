# Generated by Django 4.0.4 on 2022-05-12 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_rename_synced_stories_syn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stories',
            old_name='syn',
            new_name='synced',
        ),
    ]
