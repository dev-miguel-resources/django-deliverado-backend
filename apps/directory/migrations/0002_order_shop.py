# Generated by Django 2.2.13 on 2020-09-29 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='directory.Shop'),
            preserve_default=False,
        ),
    ]
