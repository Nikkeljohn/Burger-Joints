# Generated by Django 3.2.19 on 2023-05-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(choices=[(2, '2'), (4, '4'), (6, '6'), (8, '8'), (10, '10'), (12, '12')], default=2)),
                ('table_number', models.IntegerField()),
            ],
            options={
                'ordering': ['table_number'],
            },
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.IntegerField(choices=[(1, '12:00pm - 1:45pm'), (2, '2:00pm - 3:45pm'), (3, '4:00pm - 5:45pm'), (4, '6:00pm - 7:45pm')], default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='guests',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=105),
        ),
    ]
