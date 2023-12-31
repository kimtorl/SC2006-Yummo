# Generated by Django 4.1.7 on 2023-03-18 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YummoGroupAPI', '0006_customerprofile_icon_merchantprofile_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yummogroup',
            name='owner',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Customers'}, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL),
        ),
    ]
