# Generated by Django 4.2.4 on 2023-08-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_customer_client_username_remove_client_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='spent_money',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]