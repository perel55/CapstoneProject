# Generated by Django 5.1.1 on 2024-10-07 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barangay', '0002_residents_auth_user_alter_accounts_resident_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='bhw_id',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='officials_id',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='account_typeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barangay.account_type'),
        ),
    ]
