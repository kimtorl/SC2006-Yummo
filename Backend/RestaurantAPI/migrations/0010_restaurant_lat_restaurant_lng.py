# Generated by Django 4.1.7 on 2023-03-24 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantAPI', '0009_apply_default_cuisine'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
