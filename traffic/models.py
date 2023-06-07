
from django.db import models


class Accident(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    road_type = models.CharField(max_length=255)
    vehicle_speed = models.CharField(max_length=255)
    traffic_signal = models.CharField(max_length=255)
    road_side_far = models.CharField(max_length=255)
    injured_people_number = models.CharField(max_length=255)
    death_number = models.CharField(max_length=255)
    cost_estimation = models.CharField(max_length=255)
    traffic = models.ForeignKey('Traffic', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accident'


class AccidentImages(models.Model):
    accident = models.OneToOneField(Accident, models.DO_NOTHING, primary_key=True)
    image_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'accident_images'


class Admin(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    p_image = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Client(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    subcity = models.CharField(max_length=255)
    woreda = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    kebele = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    public_key = models.CharField(max_length=255)
    private_key = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    isappoved = models.CharField(db_column='isAppoved', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.
    admin = models.ForeignKey(Admin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'client'


class Driver(models.Model):
    accident = models.OneToOneField(Accident, models.DO_NOTHING, primary_key=True)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    subcity = models.CharField(max_length=255)
    woreda = models.CharField(max_length=255)
    kebele = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    isdrunk = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'driver'


class InjuredPeople(models.Model):
    accident = models.ForeignKey(Accident, models.DO_NOTHING)
    injurytype = models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'injured_people'


class InvolvedVehicle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    accident = models.ForeignKey(Accident, models.DO_NOTHING)
    driver_f_name = models.CharField(max_length=255)
    driver_l_name = models.CharField(max_length=255)
    owner_f_name = models.CharField(max_length=255)
    owner_l_name = models.CharField(max_length=255)
    driver_license_number = models.CharField(max_length=255)
    driver_phone = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'involved_vehicle'


class InvolvedVehiclePlate(models.Model):
    involved_vehicle = models.OneToOneField(Accident, models.DO_NOTHING, primary_key=True)
    code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'involved_vehicle_plate'


class PeoplesInInvolvedVehicle(models.Model):
    involved_vehicle = models.ForeignKey(InvolvedVehicle, models.DO_NOTHING)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'peoples_in_involved_vehicle'


class PlateNumber(models.Model):
    accident = models.OneToOneField(Accident, models.DO_NOTHING, primary_key=True)
    code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'plate_number'


class Traffic(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    p_image = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    admin = models.OneToOneField(Admin, models.DO_NOTHING)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'traffic'
