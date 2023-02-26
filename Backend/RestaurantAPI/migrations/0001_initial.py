# Generated by Django 4.1.7 on 2023-02-25 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('resID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('avg_rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('merchant', models.ForeignKey(limit_choices_to={'groups__name': 'Merchants'}, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0)),
                ('description', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(limit_choices_to={'groups__name': 'Customers'}, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='RestaurantAPI.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservID', models.AutoField(primary_key=True, serialize=False)),
                ('reserved_at', models.DateTimeField(auto_now=True)),
                ('pax', models.IntegerField()),
                ('customer', models.ForeignKey(limit_choices_to={'groups__name': 'Customers'}, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='RestaurantAPI.restaurant')),
            ],
        ),
    ]