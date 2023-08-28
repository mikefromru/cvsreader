# Generated by Django 4.2.4 on 2023-08-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_client_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='customer',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='client',
            name='item',
        ),
        migrations.RemoveField(
            model_name='client',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='client',
            name='total',
        ),
    ]
