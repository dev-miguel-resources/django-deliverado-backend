# Generated by Django 2.2.13 on 2020-10-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0004_auto_20201001_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotionshop',
            name='description',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotionshop',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
