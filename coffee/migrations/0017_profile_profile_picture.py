# Generated by Django 5.1 on 2024-12-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0016_alter_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
