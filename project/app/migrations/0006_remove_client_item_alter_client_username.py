# Generated by Django 4.2.4 on 2023-08-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_client_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='item',
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
