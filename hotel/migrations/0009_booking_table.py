# Generated by Django 3.2.19 on 2023-05-23 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0008_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(unique=True)),
                ('capacity', models.IntegerField(choices=[(2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12')], default=2)),
                ('wheelchair_accessible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['table_number'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_name', models.CharField(max_length=25)),
                ('number_of_guests', models.IntegerField(default=2)),
                ('booking_date', models.DateField()),
                ('booking_time', models.IntegerField(choices=[(1, '4:00pm - 5:00pm'), (2, '5:00pm _ 6:00pm'), (3, '6:00pm - 7:00pm'), (4, '7:00pm - 8:00pm'), (5, '8:00pm - 9:00pm'), (6, '9:00 - 10:00pm')], default=1)),
                ('booked_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_table', to='hotel.table')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['booking_date', 'booking_time'],
            },
        ),
    ]
