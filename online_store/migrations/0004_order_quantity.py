# Generated by Django 4.2.2 on 2024-01-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
