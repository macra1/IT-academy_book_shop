# Generated by Django 3.2.3 on 2021-05-23 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PublishingHouse',
            new_name='Publisher',
        ),
    ]
