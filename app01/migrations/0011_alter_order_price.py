# Generated by Django 4.1.7 on 2023-03-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_rename_number_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
