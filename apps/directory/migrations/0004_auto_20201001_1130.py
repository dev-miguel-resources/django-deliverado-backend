# Generated by Django 2.2.13 on 2020-10-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_shop_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
