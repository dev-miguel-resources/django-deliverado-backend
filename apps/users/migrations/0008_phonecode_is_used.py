# Generated by Django 2.2.13 on 2020-10-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_phonecode_type_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonecode',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
