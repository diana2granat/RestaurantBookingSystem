# Generated by Django 5.0.1 on 2024-01-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_user_remove_booking_table_booking_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
