# Generated by Django 3.2.23 on 2023-12-18 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dydx', '0003_auto_20231217_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='uniswap',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='balance',
            name='wallet_address',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
