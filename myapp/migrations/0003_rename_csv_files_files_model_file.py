# Generated by Django 5.0.6 on 2024-05-31 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_files_files_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files_model',
            old_name='csv_files',
            new_name='file',
        ),
    ]