# Generated by Django 2.2.13 on 2021-04-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210122_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='manage_menu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='manage_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='manage_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='manage_promo',
            field=models.BooleanField(default=False),
        ),
    ]
