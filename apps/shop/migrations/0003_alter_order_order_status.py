# Generated by Django 4.2.9 on 2024-02-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_watchlist_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(max_length=100),
        ),
    ]
