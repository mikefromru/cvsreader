# Generated by Django 4.2.4 on 2023-09-05 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_client_gems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='spent_money',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]