# Generated by Django 4.1 on 2022-08-08 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_remove_journal_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='favorite',
        ),
    ]