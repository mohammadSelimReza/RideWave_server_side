# Generated by Django 5.1.1 on 2024-10-04 03:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Driver', '0001_initial'),
        ('Rider', '0002_riderusermodel_birth_date_riderusermodel_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelDetailsModel',
            fields=[
                ('request_no', models.PositiveIntegerField(default=1, primary_key=True, serialize=False)),
                ('start_location', models.CharField(max_length=400)),
                ('destination_location', models.CharField(max_length=400)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(auto_now_add=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('distance', models.FloatField()),
                ('price', models.FloatField()),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('net_banking', 'Net Banking'), ('card', 'Card')], max_length=100)),
                ('payment_status', models.BooleanField(default=False)),
                ('travel_running', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Driver.driverusermodel')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rider.riderusermodel')),
            ],
        ),
        migrations.CreateModel(
            name='TravelHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_date_time', models.DateTimeField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Driver.driverusermodel')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rider.riderusermodel')),
                ('travel_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Travel.traveldetailsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TravelRequestModel',
            fields=[
                ('request_no', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('start_location', models.CharField(max_length=400)),
                ('destination_location', models.CharField(max_length=400)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('net_banking', 'Net Banking'), ('card', 'Card')], default='cash', max_length=100)),
                ('travel_vehicle', models.CharField(choices=[('bike', 'Bike'), ('cng', 'CNG'), ('car', 'Car')], max_length=100)),
                ('path_distance', models.FloatField(default='0.00')),
                ('travel_fare', models.FloatField(default='0.00')),
                ('driver_booked', models.BooleanField(default=False)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rider.riderusermodel')),
            ],
        ),
    ]