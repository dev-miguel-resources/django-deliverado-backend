# Generated by Django 2.2.13 on 2021-03-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0020_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='email',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='shop',
            name='phone',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
