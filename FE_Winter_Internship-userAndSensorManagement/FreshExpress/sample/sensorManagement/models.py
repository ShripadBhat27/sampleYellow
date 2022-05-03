from django.db import models

# Create your models here.


class Master(models.Model):
    id = models.AutoField(primary_key=True)
    # Field name made lowercase.
    sitelocation = models.CharField(db_column='siteLocation', max_length=255)
    room = models.CharField(max_length=255)
    # Field name made lowercase.
    mastername = models.CharField(db_column='masterName', max_length=255)
    # Field name made lowercase.
    installationdatetime = models.DateTimeField(
        db_column='installationDatetime')


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    # Field name made lowercase.
    masterid = models.ForeignKey(
        Master, models.DO_NOTHING, db_column='masterId')
    room = models.CharField(max_length=255)
    # Field name made lowercase.
    sensortype = models.CharField(db_column='sensorType', max_length=255)
    compressor = models.CharField(max_length=255)
    # Field name made lowercase.
    installationdatetime = models.DateTimeField(
        db_column='installationDatetime')
