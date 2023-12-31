# Generated by Django 4.1.7 on 2023-02-26 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YummoGroupAPI', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('contact_no', models.CharField(blank=True, max_length=20, null=True)),
                ('friends', models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Customers'}, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(limit_choices_to={'groups__name': 'Customers'}, on_delete=django.db.models.deletion.CASCADE, related_name='customerprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MerchantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('contact_no', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(limit_choices_to={'groups__name': 'Merchants'}, on_delete=django.db.models.deletion.CASCADE, related_name='merchantprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
