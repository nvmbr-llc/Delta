# Generated by Django 4.1.4 on 2023-09-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_alter_file_file_name_alter_file_file_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='original_file_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
