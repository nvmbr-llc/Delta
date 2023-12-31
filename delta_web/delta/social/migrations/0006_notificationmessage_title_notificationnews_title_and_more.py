# Generated by Django 4.1.4 on 2023-03-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_notificationwhatshot_notificationnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmessage',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notificationnews',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notificationreview',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='notificationwhatshot',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
