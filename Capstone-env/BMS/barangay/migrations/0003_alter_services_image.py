# Generated by Django 5.1.1 on 2024-10-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barangay', '0002_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
