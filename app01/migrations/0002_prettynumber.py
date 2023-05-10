# Generated by Django 4.1.7 on 2023-02-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('level', models.SmallIntegerField(choices=[(1, 'first'), (2, 'second'), (3, 'third')], default=1)),
                ('status', models.SmallIntegerField(choices=[(0, 'Occupied'), (1, 'Available')], default=1)),
            ],
        ),
    ]