# Generated by Django 3.2.19 on 2023-05-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Booking Table'},
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.IntegerField(default=0),
        ),
    ]
