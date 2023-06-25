# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Bid(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bid'


class BusinessAddress(models.Model):
    proposer = models.OneToOneField('Proposer', models.DO_NOTHING, primary_key=True)
    subcity = models.CharField(max_length=255)
    woreda = models.CharField(max_length=255)
    kebele = models.CharField(max_length=255)
    house_no = models.CharField(max_length=255)
    p_o_box = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'business_address'


class Claim(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=255)
    accident_id = models.CharField(max_length=255)
    total_price = models.CharField(max_length=255)
    closed_date = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.
    progress = models.IntegerField()
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    garage = models.ForeignKey('Garage', models.DO_NOTHING)
    proposer = models.ForeignKey('Proposer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'claim'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Expert(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    p_image = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    admin_id = models.IntegerField()
    is_active = models.CharField(db_column='is_Active', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expert'


class ExtraFitting(models.Model):
    vehicle = models.OneToOneField('Vehicle', models.DO_NOTHING, primary_key=True)
    radio = models.CharField(max_length=255)
    communication = models.CharField(max_length=255)
    bsd = models.CharField(db_column='BSD', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extra_fitting'


class Garage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    expert = models.ForeignKey(Expert, models.DO_NOTHING)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_approved = models.CharField(db_column='is_Approved', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garage'


class GarageBid(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bid = models.ForeignKey(Bid, models.DO_NOTHING)
    garage = models.ForeignKey(Garage, models.DO_NOTHING)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garage_bid'


class HealthContract(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contract_type = models.CharField(max_length=255)
    contract_price = models.CharField(max_length=255)
    contract_date = models.CharField(max_length=255)
    expire_date = models.CharField(max_length=255)
    proposer = models.ForeignKey('Proposer', models.DO_NOTHING)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'health_contract'


class Hospitals(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    admin = models.ForeignKey(Admin, models.DO_NOTHING)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hospitals'


class ItemGaragePrice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    garage_bid = models.ForeignKey(GarageBid, models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'item_garage_price'


class ItemsList(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    bid = models.ForeignKey(Bid, models.DO_NOTHING)
    item_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'items_list'


class OtherInsurances(models.Model):
    vehicle = models.OneToOneField('Vehicle', models.DO_NOTHING, primary_key=True)
    cancel = models.CharField(max_length=255)
    decline = models.CharField(max_length=255)
    iae = models.CharField(max_length=255)
    isc = models.CharField(max_length=255)
    refuse = models.CharField(max_length=255)
    requires = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'other_insurances'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    contract = models.ForeignKey(HealthContract, models.DO_NOTHING)
    date = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    reference_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class PreviousAccident(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    accident_date = models.CharField(max_length=255)
    vehicle_damage = models.CharField(max_length=255)
    personal_claims = models.CharField(max_length=255)
    property_damage = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'previous_accident'


class Proposer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    p_image = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proposer'


class ResidentialAddress(models.Model):
    proposer = models.OneToOneField(Proposer, models.DO_NOTHING, primary_key=True)
    subcity = models.CharField(max_length=255)
    woreda = models.CharField(max_length=255)
    kebele = models.CharField(max_length=255)
    house_no = models.CharField(max_length=255)
    p_o_box = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'residential_address'


class Treat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospitals, models.DO_NOTHING)
    proposer = models.ForeignKey(Proposer, models.DO_NOTHING)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'treat'


class TreatDocuments(models.Model):
    treat = models.OneToOneField(Treat, models.DO_NOTHING, primary_key=True)
    document = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'treat_documents'


class Vehicle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    engine_number = models.CharField(db_column='Engine_number', max_length=255)  # Field name made lowercase.
    model = models.CharField(max_length=255)
    cylindercapacity = models.CharField(max_length=255)
    manufacturedyear = models.CharField(max_length=255)
    currentestimation = models.CharField(max_length=255)
    appointmentdate = models.CharField(max_length=255)
    chassis_number = models.CharField(max_length=255)
    owner_f_name = models.CharField(max_length=255)
    owner_l_name = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    body_type = models.CharField(max_length=255)
    horse_power = models.CharField(max_length=255)
    good_capacity = models.CharField(max_length=255)
    passenger_capacity = models.CharField(max_length=255)
    bsg_action = models.CharField(db_column='BSG_action', max_length=255)  # Field name made lowercase.
    cover_required = models.CharField(max_length=255)
    drivers_covered = models.CharField(max_length=255)
    expert = models.ForeignKey(Expert, models.DO_NOTHING)
    proposer = models.ForeignKey(Proposer, models.DO_NOTHING)
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'


class VehicleContract(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vehicle = models.ForeignKey(Vehicle, models.DO_NOTHING)
    proposer = models.ForeignKey(Proposer, models.DO_NOTHING)
    contract_type = models.CharField(max_length=255)
    contract_price = models.CharField(max_length=255)
    contract_date = models.CharField(max_length=255)
    expire_date = models.CharField(max_length=255)
    is_approved = models.CharField(db_column='is_Approved', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle_contract'


class VehicleImage(models.Model):
    vehicle = models.OneToOneField(Vehicle, models.DO_NOTHING, primary_key=True)
    images = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vehicle_image'


class VehiclePlate(models.Model):
    vehicle = models.OneToOneField(Vehicle, models.DO_NOTHING, primary_key=True)
    code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vehicle_plate'
