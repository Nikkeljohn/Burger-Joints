# Generated by Django 3.2.19 on 2023-05-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
    ]
