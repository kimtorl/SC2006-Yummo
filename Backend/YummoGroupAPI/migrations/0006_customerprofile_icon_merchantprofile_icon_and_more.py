# Generated by Django 4.1.7 on 2023-03-18 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YummoGroupAPI', '0005_alter_yummogroup_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='merchantprofile',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='yummogroup',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='yummogroup',
            name='owner',
            field=models.ForeignKey(default=1, limit_choices_to={'groups__name': 'Customers'}, on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL),
        ),
    ]
