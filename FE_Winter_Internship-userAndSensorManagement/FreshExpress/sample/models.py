# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AResourcedirectory(models.Model):
    shortcode = models.CharField(db_column='ShortCode', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=10)  # Field name made lowercase.
    co_name = models.CharField(db_column='Co_Name', max_length=25)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=25)  # Field name made lowercase.
    site = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'A_ResourceDirectory'


class AlertsystemColdroomnotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    notificationid = models.CharField(db_column='NotificationID', max_length=4)  # Field name made lowercase.
    notificationdesc = models.TextField(db_column='NotificationDesc')  # Field name made lowercase.
    notificationtext = models.TextField(db_column='NotificationText')  # Field name made lowercase.
    upperlimit = models.FloatField(db_column='UpperLimit')  # Field name made lowercase.
    lowerlimit = models.FloatField(db_column='LowerLimit')  # Field name made lowercase.
    repeatafter = models.FloatField(db_column='repeatAfter')  # Field name made lowercase.
    triggervalue = models.FloatField(db_column='TriggerValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertSystem_coldroomnotification'


class AlertsystemPackhousenotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    notificationid = models.CharField(db_column='NotificationID', max_length=4)  # Field name made lowercase.
    notificationdesc = models.TextField(db_column='NotificationDesc')  # Field name made lowercase.
    notificationtext = models.TextField(db_column='NotificationText')  # Field name made lowercase.
    excursionvalue = models.FloatField(db_column='ExcursionValue')  # Field name made lowercase.
    triggervalue = models.FloatField(db_column='TriggerValue', blank=True, null=True)  # Field name made lowercase.
    repeatafter = models.FloatField(db_column='repeatAfter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertSystem_packhousenotification'


class AlertsystemPrecoolnotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    notificationid = models.CharField(db_column='NotificationID', max_length=4)  # Field name made lowercase.
    notificationdesc = models.TextField(db_column='NotificationDesc')  # Field name made lowercase.
    notificationtext = models.TextField(db_column='NotificationText')  # Field name made lowercase.
    settemp = models.FloatField(db_column='setTemp', blank=True, null=True)  # Field name made lowercase.
    delaytime = models.FloatField(db_column='delayTime', blank=True, null=True)  # Field name made lowercase.
    repeatafter = models.FloatField(db_column='repeatAfter', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertSystem_precoolnotification'


class AlertsystemStorenotifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    notificationid = models.CharField(db_column='NotificationId', max_length=4)  # Field name made lowercase.
    notificationtext = models.TextField(db_column='NotificationText')  # Field name made lowercase.
    receiverteam = models.TextField(db_column='ReceiverTeam')  # Field name made lowercase.
    notificationtime = models.DateTimeField(db_column='NotificationTime')  # Field name made lowercase.
    notificationsystem = models.TextField(db_column='NotificationSystem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertSystem_storenotifications'


class Chagent(models.Model):
    agent = models.CharField(max_length=45)
    address = models.CharField(max_length=120)
    citycode = models.IntegerField(db_column='cityCode')  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode')  # Field name made lowercase.
    mobile1 = models.IntegerField()
    mobile2 = models.IntegerField()
    gstin = models.IntegerField(db_column='GSTIN')  # Field name made lowercase.
    bankac = models.IntegerField(db_column='bankAc')  # Field name made lowercase.
    ifsccode = models.IntegerField(db_column='ifscCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHAgent'


class CropCode(models.Model):
    cropid = models.CharField(db_column='cropId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cropcode = models.CharField(db_column='cropCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cropname = models.CharField(db_column='cropName', max_length=33, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Crop_Code'


class LoginAppuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    empcode = models.CharField(db_column='empCode', unique=True, max_length=8, blank=True, null=True)  # Field name made lowercase.
    team1 = models.CharField(max_length=3, blank=True, null=True)
    team2 = models.CharField(max_length=3, blank=True, null=True)
    team3 = models.CharField(max_length=3, blank=True, null=True)
    team4 = models.CharField(max_length=3, blank=True, null=True)
    team5 = models.CharField(max_length=3, blank=True, null=True)
    team6 = models.CharField(max_length=3, blank=True, null=True)
    team7 = models.CharField(max_length=3, blank=True, null=True)
    team8 = models.CharField(max_length=3, blank=True, null=True)
    team9 = models.CharField(max_length=3, blank=True, null=True)
    team10 = models.CharField(max_length=3, blank=True, null=True)
    act_status = models.CharField(max_length=10, blank=True, null=True)
    chat_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Login_appuser'


class LoginTeamaccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    viewname = models.TextField(db_column='viewName', blank=True, null=True)  # Field name made lowercase.
    team1 = models.CharField(max_length=3, blank=True, null=True)
    team2 = models.CharField(max_length=3, blank=True, null=True)
    team3 = models.CharField(max_length=3, blank=True, null=True)
    team4 = models.CharField(max_length=3, blank=True, null=True)
    team5 = models.CharField(max_length=3, blank=True, null=True)
    team6 = models.CharField(max_length=3, blank=True, null=True)
    team7 = models.CharField(max_length=3, blank=True, null=True)
    team8 = models.CharField(max_length=3, blank=True, null=True)
    team9 = models.CharField(max_length=3, blank=True, null=True)
    team10 = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Login_teamaccess'


class PrecoolBigprecoolmodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    starthrs = models.IntegerField(db_column='startHrs')  # Field name made lowercase.
    stdtemp = models.FloatField(db_column='stdTemp')  # Field name made lowercase.
    actualtemp = models.FloatField(db_column='actualTemp')  # Field name made lowercase.
    update = models.DateTimeField(db_column='Update')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Precool_bigprecoolmodel'


class PrecoolPrecoolmodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    starthrs = models.IntegerField(db_column='startHrs')  # Field name made lowercase.
    stdtemp = models.FloatField(db_column='stdTemp')  # Field name made lowercase.
    actualtemp = models.FloatField(db_column='actualTemp')  # Field name made lowercase.
    update = models.DateTimeField(db_column='Update')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Precool_precoolmodel'


class PrecoolPrecoolresult(models.Model):
    id = models.BigAutoField(primary_key=True)
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    precooltype = models.TextField(db_column='precoolType')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime')  # Field name made lowercase.
    starttemp = models.FloatField(db_column='startTemp')  # Field name made lowercase.
    endtemp = models.FloatField(db_column='endTemp')  # Field name made lowercase.
    precoolduration = models.FloatField(db_column='PrecoolDuration', blank=True, null=True)  # Field name made lowercase.
    coolingrate = models.FloatField(db_column='coolingRate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Precool_precoolresult'


class PrecoolPrecoolsubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    onbutton = models.IntegerField(db_column='onButton')  # Field name made lowercase.
    offbutton = models.IntegerField(db_column='offButton')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Precool_precoolsubmission'


class Rfid(models.Model):
    rfidid = models.AutoField(db_column='rfidId', primary_key=True)  # Field name made lowercase.
    rfidhex = models.CharField(db_column='rfidHex', max_length=15)  # Field name made lowercase.
    srno = models.CharField(db_column='srNo', max_length=10)  # Field name made lowercase.
    application = models.CharField(db_column='Application', max_length=43)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RFID'


class Sheet1(models.Model):
    loggerid = models.IntegerField(blank=True, null=True)
    loggermake = models.CharField(max_length=6, blank=True, null=True)
    loggerserialno = models.CharField(db_column='LoggerSerialNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    usebefore = models.CharField(max_length=10, blank=True, null=True)
    invoiceno = models.CharField(db_column='invoiceNo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sheet1'


class Attendanceband(models.Model):
    uploadtime = models.DateTimeField(db_column='UploadTime')  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=20, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=20, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    uxtime = models.IntegerField(db_column='UxTime')  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendanceband'


class Attendancedata(models.Model):
    empcode = models.CharField(db_column='empCode', max_length=8)  # Field name made lowercase.
    empname = models.CharField(db_column='empName', max_length=50)  # Field name made lowercase.
    date = models.DateField()
    intime = models.DateTimeField(db_column='inTime')  # Field name made lowercase.
    outtime = models.DateTimeField(db_column='outTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attendancedata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Bankers(models.Model):
    bankid = models.AutoField(db_column='bankId', unique=True)  # Field name made lowercase.
    bankcode = models.CharField(db_column='bankCode', primary_key=True, max_length=6)  # Field name made lowercase.
    bankname = models.CharField(db_column='bankName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=45, blank=True, null=True)
    ifsccode = models.CharField(db_column='IFSCcode', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bankers'


class Boxtype(models.Model):
    boxid = models.AutoField(db_column='boxId', unique=True)  # Field name made lowercase.
    boxtypecode = models.CharField(db_column='boxTypeCode', primary_key=True, max_length=10)  # Field name made lowercase.
    boxname = models.CharField(db_column='boxName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxtype'


class Boxwt(models.Model):
    controlno = models.IntegerField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    boxsrno = models.CharField(db_column='boxSrno', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='FGcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.CharField(db_column='stationID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    empid = models.CharField(db_column='empID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate', blank=True, null=True)  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'boxwt'


class ChemicalsAnnex9(models.Model):
    chemicalid = models.AutoField(db_column='chemicalId', primary_key=True)  # Field name made lowercase.
    chemicalname = models.CharField(db_column='chemicalName', max_length=256, blank=True, null=True)  # Field name made lowercase.
    listno = models.IntegerField(db_column='listNo', blank=True, null=True)  # Field name made lowercase.
    stds = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    arfd = models.DecimalField(db_column='ARFD', max_digits=12, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    wefdate = models.DateField(db_column='wefDate', blank=True, null=True)  # Field name made lowercase.
    expdate = models.DateField(db_column='expDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chemicals_Annex9'


class City(models.Model):
    srno = models.AutoField(db_column='srNo', primary_key=True)  # Field name made lowercase.
    citycode = models.CharField(db_column='cityCode', unique=True, max_length=6, blank=True, null=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='cityName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pincode = models.CharField(max_length=128, db_collation='latin1_swedish_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Coldstorage(models.Model):
    code = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coldstorage'


class Color(models.Model):
    colorcode = models.CharField(db_column='colorCode', primary_key=True, max_length=11)  # Field name made lowercase.
    colorname = models.CharField(db_column='colorName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'color'


class CompanyFe(models.Model):
    cin = models.CharField(db_column='CIN', max_length=20)  # Field name made lowercase.
    gst = models.CharField(db_column='GST', max_length=20)  # Field name made lowercase.
    aeo = models.CharField(db_column='AEO', max_length=20)  # Field name made lowercase.
    iec = models.CharField(db_column='IEC', max_length=20)  # Field name made lowercase.
    rex = models.CharField(db_column='REX', max_length=20)  # Field name made lowercase.
    fssai = models.CharField(db_column='FSSAI', max_length=20)  # Field name made lowercase.
    udyog_aadhar = models.CharField(max_length=30)
    pan = models.CharField(db_column='PAN', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_Fe'


class Container(models.Model):
    containersealno = models.CharField(db_column='containerSealNo', max_length=15)  # Field name made lowercase.
    shippinglinecode = models.ForeignKey('Shippingline', models.DO_NOTHING, db_column='shippingLineCode')  # Field name made lowercase.
    containerno = models.CharField(db_column='containerNo', primary_key=True, max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'container'


class Containermovement(models.Model):
    invoiceno = models.CharField(db_column='invoiceNo', max_length=45)  # Field name made lowercase.
    containerno = models.CharField(db_column='containerNo', max_length=45)  # Field name made lowercase.
    vehicleno = models.CharField(db_column='vehicleNo', max_length=45)  # Field name made lowercase.
    vehicleoutjnpt = models.DateTimeField(db_column='vehicleOutJNPT', blank=True, null=True)  # Field name made lowercase.
    sitein = models.DateTimeField(db_column='siteIn', blank=True, null=True)  # Field name made lowercase.
    loadingcomplete = models.DateTimeField(db_column='loadingComplete', blank=True, null=True)  # Field name made lowercase.
    siteout = models.DateTimeField(db_column='siteOut', blank=True, null=True)  # Field name made lowercase.
    icdout = models.DateTimeField(db_column='ICDOut', blank=True, null=True)  # Field name made lowercase.
    portarrive = models.DateTimeField(db_column='portArrive', blank=True, null=True)  # Field name made lowercase.
    gatein = models.DateTimeField(db_column='gateIn', blank=True, null=True)  # Field name made lowercase.
    vesselsail = models.DateTimeField(db_column='vesselSail', blank=True, null=True)  # Field name made lowercase.
    recheddestinationport = models.DateTimeField(db_column='rechedDestinationPort', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'containerMovement'


class Containermovementnew(models.Model):
    invoiceno = models.CharField(db_column='invoiceNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    containerno = models.CharField(db_column='containerNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vehicleno = models.CharField(db_column='vehicleNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vehicleoutjnpt = models.DateTimeField(db_column='vehicleOutJNPT', blank=True, null=True)  # Field name made lowercase.
    sitein = models.DateTimeField(db_column='siteIn', blank=True, null=True)  # Field name made lowercase.
    loadingcomplete = models.DateTimeField(db_column='loadingComplete', blank=True, null=True)  # Field name made lowercase.
    siteout = models.DateTimeField(db_column='siteOut', blank=True, null=True)  # Field name made lowercase.
    icdout = models.DateTimeField(db_column='ICDOut', blank=True, null=True)  # Field name made lowercase.
    portarrive = models.DateTimeField(db_column='portArrive', blank=True, null=True)  # Field name made lowercase.
    gatein = models.DateTimeField(db_column='gateIn', blank=True, null=True)  # Field name made lowercase.
    vesselsail = models.DateTimeField(db_column='vesselSail', blank=True, null=True)  # Field name made lowercase.
    reacheddestinationport = models.DateTimeField(db_column='reachedDestinationPort', blank=True, null=True)  # Field name made lowercase.
    closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'containerMovementNew'


class Controlcompletionform(models.Model):
    controlno = models.IntegerField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    berrywt = models.DecimalField(db_column='berryWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bunchwt = models.DecimalField(db_column='bunchWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    totalwastage = models.DecimalField(db_column='totalWastage', max_digits=8, decimal_places=3)  # Field name made lowercase.
    empname = models.CharField(db_column='empName', max_length=43)  # Field name made lowercase.
    empremark = models.TextField(db_column='empRemark')  # Field name made lowercase.
    closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'controlcompletionform'


class Controlnoform(models.Model):
    controlno = models.AutoField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    growercode = models.CharField(db_column='growerCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mhcode = models.CharField(db_column='MHCode', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'controlnoform'


class Controlnostatus(models.Model):
    lineno = models.CharField(db_column='lineNo', primary_key=True, max_length=3)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'controlnostatus'


class Country(models.Model):
    countrycode = models.CharField(db_column='countryCode', primary_key=True, max_length=2)  # Field name made lowercase.
    countryname = models.CharField(db_column='countryName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Courier(models.Model):
    couriercode = models.IntegerField(db_column='CourierCode', primary_key=True)  # Field name made lowercase.
    couriername = models.CharField(db_column='CourierName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=120, blank=True, null=True)  # Field name made lowercase.
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    mobileno1 = models.CharField(db_column='mobileNo1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobileno2 = models.CharField(db_column='mobileNo2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='bankCode', blank=True, null=True)  # Field name made lowercase.
    trackurl = models.CharField(db_column='TrackURL', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courier'


class Crateqcwt(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo', blank=True, null=True)  # Field name made lowercase.
    punnetsrno = models.CharField(db_column='punnetSrNo', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='FGcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.CharField(db_column='stationID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    empid = models.CharField(db_column='empID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    craterfid = models.CharField(db_column='crateRFID', max_length=15)  # Field name made lowercase.
    grapequalityid = models.CharField(db_column='grapeQualityID', max_length=3)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate', blank=True, null=True)  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime', blank=True, null=True)  # Field name made lowercase.
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'crateqcwt'


class Crates(models.Model):
    crateid = models.AutoField(db_column='crateId', primary_key=True)  # Field name made lowercase.
    cratecode = models.CharField(unique=True, max_length=4)
    name = models.CharField(max_length=45, blank=True, null=True)
    make = models.CharField(max_length=45, blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crates'


class Crops(models.Model):
    cropid = models.AutoField(db_column='cropId', unique=True)  # Field name made lowercase.
    cropcode = models.CharField(db_column='cropCode', primary_key=True, max_length=10)  # Field name made lowercase.
    cropname = models.CharField(db_column='cropName', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crops'


class Currency(models.Model):
    currencyid = models.AutoField(db_column='currencyId', unique=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='currencyCode', primary_key=True, max_length=3)  # Field name made lowercase.
    currencyname = models.CharField(db_column='currencyName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'currency'


class Cutoff(models.Model):
    serviceid = models.AutoField(primary_key=True)
    shippingline = models.CharField(db_column='ShippingLine', max_length=45, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    service = models.CharField(unique=True, max_length=6, blank=True, null=True)
    terminal = models.TextField(blank=True, null=True)
    departureday = models.DateField(db_column='departureDay', blank=True, null=True)  # Field name made lowercase.
    gateopenreefer = models.DateField(db_column='gateOpenreefer', blank=True, null=True)  # Field name made lowercase.
    enscutoff = models.DateField(db_column='ensCutoff', blank=True, null=True)  # Field name made lowercase.
    sbcutoff = models.DateField(db_column='sbCutoff', blank=True, null=True)  # Field name made lowercase.
    gatecutoff = models.DateField(db_column='gateCutoff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cutoff'


class Destinationport(models.Model):
    portid = models.AutoField(db_column='portId', unique=True)  # Field name made lowercase.
    portcode = models.CharField(primary_key=True, max_length=6)
    portname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destinationport'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Docsupload(models.Model):
    pono = models.IntegerField(primary_key=True)
    srno = models.IntegerField(blank=True, null=True)
    docdetails = models.CharField(max_length=45, blank=True, null=True)
    filename = models.CharField(db_column='fileName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docsupload'


class Driverdocs(models.Model):
    code = models.IntegerField(primary_key=True)
    srno = models.IntegerField(blank=True, null=True)
    details = models.CharField(max_length=45, blank=True, null=True)
    filename = models.CharField(db_column='fileName', max_length=120, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'driverdocs'


class Drivers(models.Model):
    drvcode = models.IntegerField(db_column='drvCode', primary_key=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='driverName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    drivermob = models.CharField(db_column='driverMob', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobileno2 = models.CharField(db_column='MobileNo2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=120, blank=True, null=True)
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankifsccode = models.CharField(db_column='bankIFSCCode', max_length=11, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aadhar = models.CharField(max_length=12, blank=True, null=True)
    licensetype = models.IntegerField(db_column='licenseType', blank=True, null=True)  # Field name made lowercase.
    licenseno = models.CharField(db_column='licenseNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    licensedate = models.CharField(db_column='licenseDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    issuedate = models.CharField(db_column='issueDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    issueauthority = models.CharField(db_column='issueAuthority', max_length=45, blank=True, null=True)  # Field name made lowercase.
    validupto = models.CharField(db_column='validUpto', max_length=12, blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.CharField(db_column='joiningDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dob = models.CharField(db_column='DOB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    eduqual = models.CharField(db_column='eduQual', max_length=45, blank=True, null=True)  # Field name made lowercase.
    experience = models.CharField(max_length=45, blank=True, null=True)
    martialstatus = models.IntegerField(db_column='martialStatus', blank=True, null=True)  # Field name made lowercase.
    dependants = models.CharField(max_length=45, blank=True, null=True)
    refname = models.CharField(db_column='refName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    refmobile = models.CharField(db_column='refMobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    faxno = models.CharField(db_column='faxNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='webSiteURL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bankactype = models.CharField(db_column='bankACtype', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drivers'


class Employee(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True)  # Field name made lowercase.
    empcode = models.CharField(db_column='empCode', max_length=8)  # Field name made lowercase.
    empname = models.CharField(db_column='empName', max_length=45)  # Field name made lowercase.
    empemail = models.CharField(db_column='empEmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    mobile1 = models.BigIntegerField()
    mobile2 = models.BigIntegerField(blank=True, null=True)
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankifsc = models.CharField(db_column='bankIFSC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    acholdername = models.CharField(db_column='AcHolderName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aadhaar = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.DateField(db_column='joiningDate', blank=True, null=True)  # Field name made lowercase.
    eduqual = models.CharField(db_column='eduQual', max_length=45, blank=True, null=True)  # Field name made lowercase.
    experience = models.IntegerField(blank=True, null=True)
    maritalstatus = models.CharField(db_column='maritalStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dependants = models.CharField(max_length=45, blank=True, null=True)
    refname = models.CharField(db_column='refName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    refaddress = models.CharField(db_column='refAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sifacode = models.IntegerField(db_column='SIFACode', blank=True, null=True)  # Field name made lowercase.
    accesstype = models.IntegerField(db_column='accessType', blank=True, null=True)  # Field name made lowercase.
    sifaserialnumber = models.IntegerField(db_column='SIFASerialNumber', blank=True, null=True)  # Field name made lowercase.
    empshortcode = models.CharField(db_column='empShortCode', max_length=4, blank=True, null=True)  # Field name made lowercase.
    usercreated = models.IntegerField(db_column='userCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class Employee2(models.Model):
    empcode = models.IntegerField(db_column='empCode', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    groupcode = models.IntegerField(db_column='groupCode', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=120, blank=True, null=True)
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    faxno = models.CharField(db_column='faxNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bankactype = models.CharField(db_column='bankACtype', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='bankCode', blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aadhaar = models.CharField(max_length=12, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    dob = models.CharField(db_column='DOB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.CharField(db_column='joiningDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    eduqual = models.CharField(db_column='eduQual', max_length=45, blank=True, null=True)  # Field name made lowercase.
    experience = models.CharField(max_length=45, blank=True, null=True)
    martialstatus = models.IntegerField(db_column='martialStatus', blank=True, null=True)  # Field name made lowercase.
    depender = models.CharField(max_length=45, blank=True, null=True)
    refname = models.CharField(db_column='refName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    refaddress = models.CharField(db_column='refAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    accesstype = models.IntegerField(db_column='accessType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee2'


class Eseal(models.Model):
    esealid = models.IntegerField()
    make = models.CharField(max_length=20, db_collation='utf8_unicode_ci')
    serialno = models.CharField(db_column='SerialNo', max_length=20, db_collation='utf8_unicode_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eseal'


class Expinvpallet(models.Model):
    expinvno = models.IntegerField(primary_key=True)
    palletno = models.IntegerField(db_column='palletNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expinvpallet'


class Export(models.Model):
    invoiceno = models.CharField(db_column='invoiceNo', primary_key=True, max_length=7)  # Field name made lowercase.
    containerno = models.CharField(db_column='containerNo', max_length=11)  # Field name made lowercase.
    packhousename = models.CharField(db_column='packHouseName', max_length=5)  # Field name made lowercase.
    partyshortname = models.CharField(db_column='partyShortName', max_length=3)  # Field name made lowercase.
    invoicedate = models.DateField(db_column='invoiceDate')  # Field name made lowercase.
    transporter = models.CharField(max_length=15)
    vehicleno = models.CharField(db_column='vehicleNo', max_length=10)  # Field name made lowercase.
    drivername = models.CharField(db_column='driverName', max_length=15)  # Field name made lowercase.
    drivermbl = models.CharField(db_column='driverMbl', max_length=10)  # Field name made lowercase.
    product = models.CharField(max_length=15)
    chagent = models.CharField(db_column='cHAgent', max_length=50)  # Field name made lowercase.
    containersealno = models.CharField(db_column='containerSealNo', max_length=11)  # Field name made lowercase.
    shippingline = models.CharField(db_column='shippingLine', max_length=15)  # Field name made lowercase.
    vesselname = models.CharField(db_column='vesselName', max_length=20)  # Field name made lowercase.
    destinationport = models.CharField(db_column='destinationPort', max_length=50)  # Field name made lowercase.
    transhipmentport = models.CharField(db_column='transhipmentPort', max_length=50)  # Field name made lowercase.
    rfidseal = models.CharField(db_column='RFIDSeal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    serviceshipping = models.CharField(db_column='serviceShipping', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'export'


class ExportregistrationappExport(models.Model):
    invoiceno = models.CharField(db_column='invoiceNo', primary_key=True, max_length=7)  # Field name made lowercase.
    containerno = models.CharField(db_column='containerNo', max_length=11)  # Field name made lowercase.
    packhousename = models.CharField(db_column='packhouseName', max_length=5)  # Field name made lowercase.
    partyshortname = models.CharField(db_column='partyShortName', max_length=3)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='invoiceDate')  # Field name made lowercase.
    transporter = models.CharField(max_length=15)
    vehiclenumber = models.CharField(db_column='vehicleNumber', max_length=10)  # Field name made lowercase.
    drivername = models.CharField(db_column='driverName', max_length=15)  # Field name made lowercase.
    drivermbl = models.CharField(db_column='driverMbl', max_length=10)  # Field name made lowercase.
    product = models.CharField(max_length=6)
    containersealno = models.CharField(db_column='containerSealNo', max_length=11)  # Field name made lowercase.
    shippingline = models.CharField(db_column='shippingLine', max_length=5)  # Field name made lowercase.
    destinationport = models.CharField(db_column='destinationPort', max_length=50)  # Field name made lowercase.
    transhipmentport = models.CharField(db_column='transhipmentPort', max_length=50)  # Field name made lowercase.
    vesselname = models.CharField(db_column='vesselName', max_length=50)  # Field name made lowercase.
    voyageno = models.CharField(db_column='voyageNo', max_length=15)  # Field name made lowercase.
    vesseletd = models.DateTimeField(db_column='vesselETD')  # Field name made lowercase.
    vesseleta = models.DateTimeField(db_column='vesselETA')  # Field name made lowercase.
    transhipmenteta = models.DateTimeField(db_column='transhipmentETA')  # Field name made lowercase.
    transhipmentetd = models.DateTimeField(db_column='transhipmentETD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exportRegistrationApp_export'


class Exportdocs(models.Model):
    docid = models.AutoField(db_column='docId', primary_key=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=7, blank=True, null=True)  # Field name made lowercase.
    shippingbillnumber = models.CharField(db_column='shippingBillNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shippingbilldate = models.DateField(db_column='shippingBillDate', blank=True, null=True)  # Field name made lowercase.
    exchangecurrency = models.CharField(db_column='exchangeCurrency', max_length=11, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='exchangeRate', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fobvalueinr = models.DecimalField(db_column='fobValueINR', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fobvalueforex = models.DecimalField(db_column='fobValueForex', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dutydrawback = models.DecimalField(db_column='dutyDrawBack', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    blnumber = models.CharField(db_column='blNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bldate = models.DateField(db_column='blDate', blank=True, null=True)  # Field name made lowercase.
    brcno = models.CharField(db_column='brcNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    brcdate = models.DateField(db_column='brcDate', blank=True, null=True)  # Field name made lowercase.
    brcamtinfx = models.DecimalField(db_column='brcAmtInFx', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    brccurrency = models.CharField(db_column='brcCurrency', max_length=12, blank=True, null=True)  # Field name made lowercase.
    egmno = models.CharField(db_column='egmNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    egmdate = models.DateField(db_column='egmDate', blank=True, null=True)  # Field name made lowercase.
    phytono = models.CharField(db_column='phytoNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phytodate = models.DateField(db_column='phytoDate', blank=True, null=True)  # Field name made lowercase.
    buyer = models.CharField(max_length=20, blank=True, null=True)
    couriername = models.CharField(max_length=20, blank=True, null=True)
    courierbooking = models.CharField(db_column='courierBooking', max_length=20, blank=True, null=True)  # Field name made lowercase.
    courierbookingdate = models.DateField(db_column='courierBookingDate', blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(max_length=50, blank=True, null=True)
    trackingno = models.CharField(db_column='trackingNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    poddeliverydate = models.DateField(db_column='podDeliveryDate', blank=True, null=True)  # Field name made lowercase.
    deliverystatus = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exportdocs'


class Exportinv(models.Model):
    expinvno = models.CharField(db_column='expInvNo', primary_key=True, max_length=7)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    buyerpono = models.IntegerField(db_column='buyerPOno', blank=True, null=True)  # Field name made lowercase.
    containerno = models.CharField(db_column='containerNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    shiplinecode = models.CharField(max_length=4, blank=True, null=True)
    vehicleno = models.CharField(db_column='vehicleNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    drivername = models.CharField(db_column='driverName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    drivermobile = models.CharField(db_column='driverMobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    loadstartdate = models.DateField(db_column='loadStartDate', blank=True, null=True)  # Field name made lowercase.
    loadstarttime = models.TimeField(db_column='loadStartTime', blank=True, null=True)  # Field name made lowercase.
    empcode = models.IntegerField(db_column='empCode', blank=True, null=True)  # Field name made lowercase.
    securityperson = models.CharField(db_column='securityPerson', max_length=45, blank=True, null=True)  # Field name made lowercase.
    exitdate = models.DateField(db_column='exitDate', blank=True, null=True)  # Field name made lowercase.
    exittime = models.TimeField(db_column='exitTime', blank=True, null=True)  # Field name made lowercase.
    excisesealno = models.CharField(db_column='exciseSealNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    shipsealno = models.CharField(db_column='shipSealNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    deviceid1 = models.CharField(db_column='deviceID1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    palletno1 = models.IntegerField(db_column='palletNo1', blank=True, null=True)  # Field name made lowercase.
    deviceid2 = models.CharField(db_column='deviceID2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    palletno2 = models.IntegerField(db_column='palletNo2', blank=True, null=True)  # Field name made lowercase.
    deviceid3 = models.CharField(db_column='deviceID3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    palletno3 = models.IntegerField(db_column='palletNo3', blank=True, null=True)  # Field name made lowercase.
    donagebags = models.IntegerField(db_column='donageBags', blank=True, null=True)  # Field name made lowercase.
    destportcode = models.CharField(db_column='destPortCode', max_length=6)  # Field name made lowercase.
    containertemp = models.DecimalField(db_column='containerTemp', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exportinv'


class Farmvisit(models.Model):
    visitno = models.IntegerField(db_column='visitNo', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    growercode = models.IntegerField(db_column='growerCode', blank=True, null=True)  # Field name made lowercase.
    empcode = models.IntegerField(db_column='empCode', blank=True, null=True)  # Field name made lowercase.
    exptyield = models.IntegerField(db_column='exptYield', blank=True, null=True)  # Field name made lowercase.
    marketcatg = models.CharField(db_column='marketCatg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    harvestdate = models.DateField(db_column='harvestDate', blank=True, null=True)  # Field name made lowercase.
    cratetype = models.IntegerField(db_column='crateType', blank=True, null=True)  # Field name made lowercase.
    reqdcrates = models.IntegerField(db_column='reqdCrates', blank=True, null=True)  # Field name made lowercase.
    vehiclecode = models.IntegerField(db_column='vehicleCode', blank=True, null=True)  # Field name made lowercase.
    hrvstteamcode = models.IntegerField(db_column='hrvstTeamCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'farmvisit'


class Fgbom(models.Model):
    bomid = models.AutoField(db_column='bomId', primary_key=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='FGcode', max_length=10)  # Field name made lowercase.
    pmitemcode = models.CharField(db_column='PMitemcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pmdesc1 = models.CharField(db_column='PMDesc1', max_length=40)  # Field name made lowercase.
    pmdesc2 = models.CharField(db_column='PMDesc2', max_length=40)  # Field name made lowercase.
    qty = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'fgbom'


class Fgstatus(models.Model):
    lineno = models.IntegerField(db_column='lineNo', primary_key=True)  # Field name made lowercase.
    fgcode = models.IntegerField(db_column='FGcode', blank=True, null=True)  # Field name made lowercase.
    vremarks = models.TextField(db_column='vRemarks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fgstatus'


class Finalqc(models.Model):
    controlno = models.IntegerField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    berysizemostly = models.IntegerField(db_column='berySizeMostly', blank=True, null=True)  # Field name made lowercase.
    berysizesome = models.IntegerField(db_column='berySizeSome', blank=True, null=True)  # Field name made lowercase.
    colormostly = models.IntegerField(db_column='colorMostly', blank=True, null=True)  # Field name made lowercase.
    colorsome = models.IntegerField(db_column='colorSome', blank=True, null=True)  # Field name made lowercase.
    stemqmostly = models.CharField(db_column='stemQMostly', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stemqsome = models.CharField(db_column='stemQSome', max_length=20, blank=True, null=True)  # Field name made lowercase.
    brixmostly = models.DecimalField(db_column='brixMostly', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    brixsome = models.DecimalField(db_column='brixSome', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    qcdate = models.CharField(db_column='qcDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    qctime = models.CharField(db_column='qcTime', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finalqc'


class Finishedgoods(models.Model):
    fgcode = models.CharField(db_column='FGcode', primary_key=True, max_length=15)  # Field name made lowercase.
    fgname = models.CharField(db_column='FGname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fgdescription = models.CharField(db_column='FGdescription', max_length=50)  # Field name made lowercase.
    fgpacktype = models.CharField(db_column='FGPackType', max_length=50)  # Field name made lowercase.
    fgunit = models.CharField(db_column='FGUnit', max_length=10, blank=True, null=True)  # Field name made lowercase.
    grosswt = models.FloatField(db_column='grossWt', blank=True, null=True)  # Field name made lowercase.
    emptywttare = models.DecimalField(db_column='emptyWtTare', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.FloatField(db_column='netWt', blank=True, null=True)  # Field name made lowercase.
    hsn_code = models.CharField(db_column='HSN Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    barcode = models.CharField(max_length=15, blank=True, null=True)
    boxtypecode = models.CharField(db_column='boxTypeCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punnet_bagcount = models.IntegerField(db_column='punnet_bagCount', blank=True, null=True)  # Field name made lowercase.
    minwt = models.DecimalField(db_column='minWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    maxwt = models.DecimalField(db_column='maxWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    avgtare = models.DecimalField(db_column='avgTare', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    singleberrywt = models.DecimalField(db_column='singleBerryWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    minboxwt = models.DecimalField(db_column='minBoxWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    maxboxwt = models.DecimalField(db_column='maxBoxWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    avgboxtare = models.DecimalField(db_column='avgBoxTare', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    singlebunchwt = models.DecimalField(db_column='singleBunchWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    max_box_per_pallet_regular = models.IntegerField(db_column='max box per pallet Regular', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    box_per_paller_small = models.IntegerField(db_column='box per paller Small', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'finishedgoods'


class Foreighnporep(models.Model):
    pono = models.IntegerField(db_column='poNo', primary_key=True)  # Field name made lowercase.
    srno = models.IntegerField(blank=True, null=True)
    rptdetails = models.CharField(db_column='rptDetails', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foreighnporep'


class Foreignbuyer(models.Model):
    foreignbuyerid = models.AutoField(db_column='foreignBuyerId', unique=True)  # Field name made lowercase.
    foreignbuyercode = models.CharField(db_column='foreignBuyerCode', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    fbemailid = models.CharField(max_length=43)
    notifypartyname_addr = models.CharField(db_column='notifyPartyName&Addr', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='currencyCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fbphoneno = models.CharField(db_column='fbPhoneNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    notifyphoneno = models.CharField(db_column='notifyPhoneNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='webSiteURL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    po_terms = models.CharField(db_column='PO_terms', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foreignbuyer'


class Foreignpo(models.Model):
    pono = models.IntegerField(db_column='poNo', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    buyercode = models.CharField(db_column='buyerCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='FGcode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    orderqty = models.IntegerField(db_column='orderQty', blank=True, null=True)  # Field name made lowercase.
    orderqtyunit = models.CharField(db_column='OrderQtyUnit', max_length=4)  # Field name made lowercase.
    color = models.IntegerField(blank=True, null=True)
    po_price = models.FloatField(db_column='PO_Price')  # Field name made lowercase.
    po_pricevalidity = models.DateField(db_column='PO_PriceValidity')  # Field name made lowercase.
    poterms = models.CharField(db_column='POTerms', max_length=15)  # Field name made lowercase.
    po_currency = models.CharField(db_column='PO_Currency', max_length=8)  # Field name made lowercase.
    advperbox = models.DecimalField(db_column='AdvPerBox', max_digits=8, decimal_places=2)  # Field name made lowercase.
    size = models.IntegerField(blank=True, null=True)
    brix = models.DecimalField(max_digits=7, decimal_places=3, blank=True, null=True)
    minpackwt = models.DecimalField(db_column='minPackWt', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    maxboxpallet = models.IntegerField(db_column='MaxBoxPallet', blank=True, null=True)  # Field name made lowercase.
    advduefmbl = models.IntegerField(db_column='AdvDuefmBL', blank=True, null=True)  # Field name made lowercase.
    finalsalefmbl = models.IntegerField(db_column='FinalSalefmBL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'foreignpo'


class Globalgap(models.Model):
    growercode = models.IntegerField(db_column='growerCode', primary_key=True)  # Field name made lowercase.
    certno = models.CharField(db_column='certNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    validto = models.DateField(db_column='validTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'globalgap'


class Groups1(models.Model):
    groupcode = models.CharField(db_column='groupCode', primary_key=True, max_length=2)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups1'


class Growerplots(models.Model):
    growercode = models.IntegerField(db_column='growerCode', primary_key=True)  # Field name made lowercase.
    plotno = models.IntegerField(blank=True, null=True)
    regnomhcode = models.CharField(db_column='regnoMHcode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ownername = models.CharField(db_column='ownerName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cropcode = models.IntegerField(db_column='cropCode', blank=True, null=True)  # Field name made lowercase.
    varietycode = models.IntegerField(db_column='varietyCode', blank=True, null=True)  # Field name made lowercase.
    gatno = models.CharField(db_column='gatNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    plants = models.IntegerField(blank=True, null=True)
    plantdist = models.IntegerField(db_column='plantDist', blank=True, null=True)  # Field name made lowercase.
    rowdist = models.IntegerField(db_column='rowDist', blank=True, null=True)  # Field name made lowercase.
    graft = models.IntegerField(blank=True, null=True)
    plantationyr = models.IntegerField(db_column='plantationYr', blank=True, null=True)  # Field name made lowercase.
    globalgap = models.IntegerField(db_column='globalGap', blank=True, null=True)  # Field name made lowercase.
    number_4bqty = models.IntegerField(db_column='4BQty', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'growerplots'


class Growers(models.Model):
    growerid = models.AutoField(db_column='growerId', unique=True)  # Field name made lowercase.
    growercode = models.CharField(db_column='growerCode', primary_key=True, max_length=6)  # Field name made lowercase.
    growername = models.CharField(db_column='growerName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mhcode = models.CharField(db_column='MHCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mhcode2 = models.CharField(db_column='MHCode2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mhcode3 = models.CharField(db_column='MHCode3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mhcode4 = models.CharField(db_column='MHCode4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ggnno = models.CharField(db_column='GGNno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ggnname = models.CharField(db_column='GGNname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ggnvalidupto = models.DateField(db_column='ggnValidUpto', blank=True, null=True)  # Field name made lowercase.
    ggncertifiedfeother = models.CharField(db_column='GGNCertifiedFEOther', max_length=43, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=120, blank=True, null=True)
    place = models.CharField(max_length=20, blank=True, null=True)
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='bankCode', blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aadhar = models.CharField(db_column='Aadhar', max_length=12, blank=True, null=True)  # Field name made lowercase.
    longlat = models.CharField(db_column='longLat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    landmark = models.CharField(db_column='landMark', max_length=45, blank=True, null=True)  # Field name made lowercase.
    distance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'growers'


class Harvesting(models.Model):
    srno = models.IntegerField()
    controlno = models.IntegerField(db_column='controlNo')  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID')  # Field name made lowercase.
    emprfid = models.IntegerField(db_column='empRFID')  # Field name made lowercase.
    craterfid = models.IntegerField(db_column='crateRFID')  # Field name made lowercase.
    hardate = models.CharField(db_column='harDate', max_length=12)  # Field name made lowercase.
    hartime = models.CharField(db_column='harTime', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvesting'


class Harvestpo(models.Model):
    pono = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    labpono = models.IntegerField(db_column='labPOno', blank=True, null=True)  # Field name made lowercase.
    vehiclecode = models.IntegerField(db_column='vehicleCode', blank=True, null=True)  # Field name made lowercase.
    drivercode = models.IntegerField(db_column='driverCode', blank=True, null=True)  # Field name made lowercase.
    cratetypecode = models.IntegerField(db_column='crateTypeCode', blank=True, null=True)  # Field name made lowercase.
    cratesqty = models.IntegerField(db_column='cratesQty', blank=True, null=True)  # Field name made lowercase.
    empcode = models.IntegerField(db_column='empCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'harvestpo'


class Harvestteam(models.Model):
    teamcode = models.IntegerField(db_column='teamCode', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    uploadfile = models.CharField(db_column='uploadFile', max_length=120, blank=True, null=True)  # Field name made lowercase.
    bankactype = models.CharField(db_column='bankACtype', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='bankCode', blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'harvestteam'


class Inward(models.Model):
    controlno = models.IntegerField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    date = models.CharField(max_length=12, blank=True, null=True)
    arrivaltime = models.CharField(max_length=12, blank=True, null=True)
    pono = models.IntegerField(blank=True, null=True)
    departdate = models.CharField(db_column='departDate', max_length=12)  # Field name made lowercase.
    departtime = models.CharField(db_column='departTime', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cratetypecode = models.IntegerField(db_column='crateTypeCode', blank=True, null=True)  # Field name made lowercase.
    filledcrates = models.IntegerField(db_column='filledCrates', blank=True, null=True)  # Field name made lowercase.
    emptycrates = models.IntegerField(db_column='emptyCrates', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=120, blank=True, null=True)
    begintime = models.TimeField(db_column='beginTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    wastberyactual = models.DecimalField(db_column='wastBeryActual', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    wasteberystd = models.DecimalField(db_column='wasteBeryStd', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    wasteberydiff = models.DecimalField(db_column='wasteBeryDiff', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    wastebunchactual = models.DecimalField(db_column='wasteBunchActual', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    wastebunchstd = models.DecimalField(db_column='wasteBunchStd', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    wastebunchdiff = models.DecimalField(db_column='wasteBunchDiff', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    lcode1 = models.CharField(db_column='LCODE1', max_length=10)  # Field name made lowercase.
    lcode2 = models.CharField(db_column='LCODE2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    totalboxes = models.IntegerField(db_column='totalBoxes', blank=True, null=True)  # Field name made lowercase.
    totalpallets = models.IntegerField(db_column='totalPallets', blank=True, null=True)  # Field name made lowercase.
    balanceboxes = models.IntegerField(db_column='balanceBoxes', blank=True, null=True)  # Field name made lowercase.
    growercode = models.IntegerField(db_column='growerCode', blank=True, null=True)  # Field name made lowercase.
    vehiclecode = models.IntegerField(db_column='vehicleCode', blank=True, null=True)  # Field name made lowercase.
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inward'
        unique_together = (('controlno', 'lcode1'),)


class Inwardqc(models.Model):
    controlno = models.IntegerField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    berysizemostly = models.IntegerField(db_column='berySizeMostly', blank=True, null=True)  # Field name made lowercase.
    berysizesome = models.IntegerField(db_column='berySizeSome', blank=True, null=True)  # Field name made lowercase.
    colormostly = models.IntegerField(db_column='colorMostly', blank=True, null=True)  # Field name made lowercase.
    colorsome = models.IntegerField(db_column='colorSome', blank=True, null=True)  # Field name made lowercase.
    stemqmostly = models.CharField(db_column='stemQMostly', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stemqsome = models.CharField(db_column='stemQSome', max_length=20, blank=True, null=True)  # Field name made lowercase.
    brixmostly = models.DecimalField(db_column='brixMostly', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    brixsome = models.DecimalField(db_column='brixSome', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    qcdate = models.CharField(db_column='qcDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    qctime = models.CharField(db_column='qcTime', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inwardqc'


class Inweight(models.Model):
    srno = models.AutoField(primary_key=True)
    controlno = models.IntegerField(db_column='controlNo', blank=True, null=True)  # Field name made lowercase.
    cratetypecode = models.IntegerField(db_column='crateTypeCode', blank=True, null=True)  # Field name made lowercase.
    cratesqty = models.IntegerField(db_column='cratesQty', blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate', blank=True, null=True)  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime', blank=True, null=True)  # Field name made lowercase.
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inweight'


class Kittingcrates(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo', blank=True, null=True)  # Field name made lowercase.
    punnetsrno = models.IntegerField(db_column='punnetSrNo', blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    craterfid = models.CharField(db_column='crateRFID', max_length=15)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate', blank=True, null=True)  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime', blank=True, null=True)  # Field name made lowercase.
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kittingcrates'


class Knitterband(models.Model):
    stationid = models.CharField(db_column='stationID', max_length=20)  # Field name made lowercase.
    empid = models.CharField(db_column='empID', max_length=12)  # Field name made lowercase.
    emp2id = models.CharField(db_column='emp2ID', max_length=12)  # Field name made lowercase.
    craterfid = models.CharField(db_column='crateRFID', max_length=15)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate')  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime')  # Field name made lowercase.
    vtimestamp = models.DateTimeField()
    srno = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'knitterband'


class Labpo(models.Model):
    labpono = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    visitno = models.IntegerField(db_column='visitNo', blank=True, null=True)  # Field name made lowercase.
    labcode = models.IntegerField(db_column='labCode', blank=True, null=True)  # Field name made lowercase.
    cbqty = models.IntegerField(db_column='CBQty', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='dueDate', blank=True, null=True)  # Field name made lowercase.
    rmpstatus = models.IntegerField(db_column='RMPStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labpo'


class Labresults(models.Model):
    srno = models.AutoField(primary_key=True)
    srannex9 = models.CharField(db_column='SrAnnex9', max_length=10, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    detpesticide = models.CharField(db_column='DetPesticide', max_length=256, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    mg_kg = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    eu_mrl = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    loq = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    mrl_percentage = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    arfd_value = models.DecimalField(db_column='Arfd_Value', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    intake = models.DecimalField(db_column='Intake', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    arfd_percentage = models.DecimalField(db_column='ARFD_Percentage', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=30, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    seal_no = models.CharField(db_column='Seal_No', max_length=12, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    sample_no = models.CharField(db_column='Sample_no', max_length=15, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    farmer_name = models.CharField(db_column='Farmer_name', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    date_sampling = models.DateField(blank=True, null=True)
    farmer_address = models.TextField(db_column='Farmer_Address', db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    farm_reg_no = models.CharField(db_column='Farm_Reg_no', max_length=20, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    exporter_name = models.CharField(db_column='Exporter_Name', max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    variety = models.CharField(db_column='Variety', max_length=20, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    number_4b_qty = models.DecimalField(db_column='4B_Qty', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    brix = models.DecimalField(db_column='Brix', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fe_po = models.CharField(db_column='FE_PO', max_length=30, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labresults'


class Labs(models.Model):
    labcode = models.IntegerField(db_column='labCode', primary_key=True)  # Field name made lowercase.
    labname = models.CharField(db_column='labName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=120, blank=True, null=True)
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='phoneNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    faxno = models.CharField(db_column='faxNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='webSiteURL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bankactype = models.CharField(db_column='bankACtype', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='bankCode', blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    langitude = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    landmark = models.CharField(max_length=40, blank=True, null=True)
    surveyer1name = models.CharField(db_column='surveyer1Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surveyer1mobile = models.CharField(db_column='surveyer1Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    surveyer2name = models.CharField(db_column='surveyer2Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surveyer2mobile = models.CharField(db_column='surveyer2Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    surveyer3name = models.CharField(db_column='surveyer3Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    surveyer3mobile = models.CharField(db_column='surveyer3Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    acct1name = models.CharField(db_column='acct1Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    acct1mobile = models.CharField(db_column='acct1Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    acct2name = models.CharField(db_column='acct2Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    acct2mobile = models.CharField(db_column='acct2Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lab1name = models.CharField(db_column='lab1Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lab1mobile = models.CharField(db_column='lab1Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lab2name = models.CharField(db_column='lab2Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lab2mobile = models.CharField(db_column='lab2Mobile', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labs'


class Logger(models.Model):
    loggerid = models.IntegerField(primary_key=True)
    loggermake = models.CharField(max_length=20)
    loggerserialno = models.CharField(db_column='LoggerSerialNo', max_length=20)  # Field name made lowercase.
    usebefore = models.DateField()
    invoiceno = models.CharField(db_column='invoiceNo', max_length=17, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logger'


class Materialinward(models.Model):
    controlno = models.IntegerField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    lotcode = models.CharField(db_column='lotCode', max_length=15)  # Field name made lowercase.
    inwardtime = models.CharField(db_column='inwardTime', max_length=15)  # Field name made lowercase.
    ionitemtype = models.CharField(db_column='ionItemType', max_length=10)  # Field name made lowercase.
    lcode1 = models.CharField(db_column='LCODE1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lcode2 = models.CharField(db_column='LCODE2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    formfilledby = models.CharField(db_column='formFilledBy', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materialinward'


class Module(models.Model):
    mod_modulegroupcode = models.CharField(primary_key=True, max_length=25)
    mod_modulegroupname = models.CharField(max_length=50)
    mod_modulecode = models.CharField(unique=True, max_length=25)
    mod_modulename = models.CharField(max_length=50)
    mod_modulegrouporder = models.IntegerField()
    mod_moduleorder = models.IntegerField()
    mod_modulepagename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'module'
        unique_together = (('mod_modulegroupcode', 'mod_modulecode'),)


class Mrjsalaryrate(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    role = models.IntegerField(db_column='Role')  # Field name made lowercase.
    rsperday = models.IntegerField(db_column='rsPerDay')  # Field name made lowercase.
    reperhour = models.IntegerField(db_column='rePerHour')  # Field name made lowercase.
    repermonth = models.IntegerField(db_column='rePerMonth')  # Field name made lowercase.
    computingfreq = models.CharField(db_column='computingFreq', max_length=10)  # Field name made lowercase.
    mrjsalaryrate = models.CharField(db_column='mrjSalaryRate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mrjSalaryRate'


class Nsksalaryrate(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    phladies01 = models.IntegerField(db_column='phLadies01')  # Field name made lowercase.
    phladies02 = models.IntegerField(db_column='phLadies02')  # Field name made lowercase.
    phladies03 = models.IntegerField(db_column='phLadies03')  # Field name made lowercase.
    security = models.IntegerField()
    phboysiktajul = models.IntegerField(db_column='phBoysIktajul')  # Field name made lowercase.
    phboyslocal = models.IntegerField(db_column='phBoysLocal')  # Field name made lowercase.
    harvester = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nskSalaryRate'


class Nsksalaryratedefault(models.Model):
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    phladies01 = models.IntegerField(db_column='phLadies01')  # Field name made lowercase.
    phladies02 = models.IntegerField(db_column='phLadies02')  # Field name made lowercase.
    phladies03 = models.IntegerField(db_column='phLadies03')  # Field name made lowercase.
    security = models.IntegerField()
    phboysiktajul = models.IntegerField(db_column='phBoysIktajul')  # Field name made lowercase.
    phboyslocal = models.IntegerField(db_column='phBoysLocal')  # Field name made lowercase.
    harvester = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nskSalaryRateDefault'


class OtherTable(models.Model):
    tableid = models.AutoField(db_column='tableID', primary_key=True)  # Field name made lowercase.
    tablename = models.TextField(db_column='tableName')  # Field name made lowercase.
    user_input = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'other_table'


class Outward(models.Model):
    controlno = models.AutoField(db_column='controlNo', primary_key=True)  # Field name made lowercase.
    site = models.CharField(max_length=15)
    crop = models.CharField(max_length=15, blank=True, null=True)
    variety = models.CharField(max_length=15, blank=True, null=True)
    drivername = models.CharField(db_column='driverName', max_length=30)  # Field name made lowercase.
    vehicalname = models.CharField(db_column='vehicalName', max_length=30)  # Field name made lowercase.
    currenttime = models.DateTimeField(db_column='currentTime')  # Field name made lowercase.
    formfilledby = models.CharField(db_column='formFilledBy', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'outward'


class Palletmast(models.Model):
    palletid = models.AutoField(db_column='palletId', primary_key=True)  # Field name made lowercase.
    palletecode = models.CharField(db_column='palleteCode', unique=True, max_length=6)  # Field name made lowercase.
    palletdetails = models.CharField(db_column='palletDetails', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='fgCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    maxqty = models.DecimalField(db_column='maxQty', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'palletmast'


class Pallets(models.Model):
    palletid = models.AutoField(db_column='palletId', primary_key=True)  # Field name made lowercase.
    palletecode = models.CharField(db_column='palleteCode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo', blank=True, null=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='fgCode', max_length=15)  # Field name made lowercase.
    boxes = models.IntegerField(blank=True, null=True)
    isselected = models.IntegerField(db_column='isSelected')  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pallets'


class Party(models.Model):
    partyshortcode = models.CharField(db_column='partyShortCode', primary_key=True, max_length=5)  # Field name made lowercase.
    partyname = models.CharField(db_column='partyName', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'party'


class Pminward(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    site = models.IntegerField()
    invoiceno = models.CharField(db_column='invoiceNo', max_length=15)  # Field name made lowercase.
    invoicedate = models.DateField(db_column='invoiceDate')  # Field name made lowercase.
    invoicevalue = models.CharField(db_column='invoiceValue', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmInward'


class PmVendor(models.Model):
    vendorcode = models.CharField(db_column='VendorCode', primary_key=True, max_length=6)  # Field name made lowercase.
    venname = models.CharField(db_column='VenName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=120, blank=True, null=True)
    citycode = models.CharField(db_column='cityCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    mobileno1 = models.CharField(db_column='mobileNo1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobileno2 = models.CharField(db_column='mobileNo2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.CharField(db_column='bankCode', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pm_vendor'


class Pmmaterial(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    invoiceno = models.CharField(db_column='invoiceNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(max_length=6)
    itemname = models.CharField(db_column='itemName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=100, blank=True, null=True)
    unitcode = models.CharField(db_column='unitCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hscode = models.CharField(max_length=20, blank=True, null=True)
    vendorcode1 = models.CharField(db_column='VendorCode1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vendorcode2 = models.CharField(db_column='VendorCode2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specs = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pmmaterial'


class PomaxDetections(models.Model):
    pono = models.IntegerField(primary_key=True)
    max_field = models.CharField(db_column='max%', max_length=2, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    maxdetections = models.CharField(db_column='maxDetections', max_length=2, blank=True, null=True)  # Field name made lowercase.
    other_conditions = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'pomax_detections'


class Ports(models.Model):
    portid = models.AutoField(db_column='portId', unique=True)  # Field name made lowercase.
    destinationportcode = models.CharField(db_column='destinationPortCode', primary_key=True, max_length=3)  # Field name made lowercase.
    destinationportname = models.CharField(db_column='destinationPortName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='countryCode', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ports'


class Precooling(models.Model):
    entryno = models.IntegerField(db_column='entryNo', primary_key=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    precollingno = models.IntegerField(db_column='precollingNo', blank=True, null=True)  # Field name made lowercase.
    loaddate = models.DateField(db_column='loadDate', blank=True, null=True)  # Field name made lowercase.
    loadtime = models.TimeField(db_column='loadTime', blank=True, null=True)  # Field name made lowercase.
    loadempcode = models.IntegerField(db_column='loadEmpCode', blank=True, null=True)  # Field name made lowercase.
    totalpallets = models.IntegerField(db_column='totalPallets', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    endempcode = models.IntegerField(db_column='endEmpCode', blank=True, null=True)  # Field name made lowercase.
    berrytemp = models.DecimalField(db_column='berryTemp', max_digits=7, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(max_length=120, blank=True, null=True)
    coldstoragecode = models.IntegerField(db_column='coldStorageCode', blank=True, null=True)  # Field name made lowercase.
    coldstoragedate = models.DateField(db_column='coldStorageDate', blank=True, null=True)  # Field name made lowercase.
    coldstoragetime = models.TimeField(db_column='coldStorageTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precooling'


class Precoolpallets(models.Model):
    entryno = models.IntegerField(db_column='entryNo', primary_key=True)  # Field name made lowercase.
    palletno = models.IntegerField(db_column='palletNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precoolpallets'


class Punnettype(models.Model):
    punnetid = models.AutoField(db_column='punnetId', primary_key=True)  # Field name made lowercase.
    punnetcode = models.CharField(db_column='punnetCode', unique=True, max_length=6)  # Field name made lowercase.
    punnetname = models.CharField(db_column='punnetName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    capacity = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punnettype'


class Punnetwt(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    controlno = models.DecimalField(db_column='controlNo', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    weighttype = models.CharField(db_column='weightType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    punnetsrno = models.IntegerField(db_column='punnetSrNo', blank=True, null=True)  # Field name made lowercase.
    fgcode = models.CharField(db_column='FGcode', max_length=15, blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.DecimalField(db_column='stationID', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    empid = models.DecimalField(db_column='empID', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    craterfid = models.CharField(db_column='crateRFID', max_length=15)  # Field name made lowercase.
    grapequalityid = models.CharField(db_column='grapeQualityID', max_length=3)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate', blank=True, null=True)  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime', blank=True, null=True)  # Field name made lowercase.
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'punnetwt'


class PunnetwtEmpty(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo', blank=True, null=True)  # Field name made lowercase.
    punnetsrno = models.IntegerField(db_column='punnetSrNo', blank=True, null=True)  # Field name made lowercase.
    fgcode = models.IntegerField(db_column='FGcode', blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    wtdate = models.DateField(db_column='wtDate', blank=True, null=True)  # Field name made lowercase.
    wttime = models.TimeField(db_column='wtTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'punnetwt-empty'


class Purtype(models.Model):
    purid = models.AutoField(db_column='purId', primary_key=True)  # Field name made lowercase.
    purtypecode = models.CharField(db_column='purTypeCode', unique=True, max_length=20, db_collation='utf8mb4_general_ci')  # Field name made lowercase.
    purtypename = models.TextField(db_column='purTypeName', db_collation='utf8mb4_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purType'


class Qccode(models.Model):
    srno = models.AutoField(primary_key=True)
    qcno = models.IntegerField()
    qcremark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'qccode'


class RelInvVar(models.Model):
    invvarid = models.AutoField(db_column='invVarid', primary_key=True)  # Field name made lowercase.
    invoice = models.ForeignKey(Export, models.DO_NOTHING, db_column='invoice')
    varietycode = models.ForeignKey('Variety', models.DO_NOTHING, db_column='varietyCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rel_Inv_Var'


class RelInvoiceFg(models.Model):
    invoiceid = models.AutoField(db_column='invoiceId', primary_key=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=15)  # Field name made lowercase.
    fgcode = models.CharField(db_column='fgCode', max_length=15)  # Field name made lowercase.
    boxcode = models.CharField(db_column='boxCode', max_length=15)  # Field name made lowercase.
    boxqty = models.IntegerField(db_column='boxQty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rel_Invoice_fg'


class RelControlnoFgcode(models.Model):
    relid = models.AutoField(db_column='relId', primary_key=True)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo')  # Field name made lowercase.
    fgcode = models.CharField(db_column='fgCode', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rel_controlNo_fgCode'


class RelOutwardCrate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    controlno = models.IntegerField(db_column='controlNo')  # Field name made lowercase.
    cratetype = models.CharField(db_column='crateType', max_length=30)  # Field name made lowercase.
    crateqty = models.IntegerField(db_column='crateQty')  # Field name made lowercase.
    inwardqty = models.IntegerField(db_column='inwardQty', blank=True, null=True)  # Field name made lowercase.
    emptycratesarrived = models.IntegerField(db_column='emptyCratesArrived', blank=True, null=True)  # Field name made lowercase.
    missingcrates = models.IntegerField(db_column='missingCrates', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rel_outward_crate'


class Remittance(models.Model):
    remittanceid = models.AutoField(db_column='remittanceId', primary_key=True)  # Field name made lowercase.
    prepaymenttoreceive = models.DecimalField(db_column='prePaymentToReceive', max_digits=8, decimal_places=3)  # Field name made lowercase.
    advanceamount = models.DecimalField(db_column='advanceAmount', max_digits=8, decimal_places=3)  # Field name made lowercase.
    advancedreceiveddata = models.DateField(db_column='advancedReceivedData')  # Field name made lowercase.
    balancetoreceive = models.DecimalField(db_column='balanceToReceive', max_digits=8, decimal_places=3)  # Field name made lowercase.
    finalpaymentamount = models.DecimalField(db_column='finalPaymentAmount', max_digits=8, decimal_places=3)  # Field name made lowercase.
    finalpaymentdate = models.DateField(db_column='finalPaymentDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'remittance'


class Rmpstatus(models.Model):
    labpono = models.IntegerField(db_column='labPOno', primary_key=True)  # Field name made lowercase.
    entryno = models.IntegerField(db_column='entryNo', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    labcode = models.IntegerField(db_column='labCode', blank=True, null=True)  # Field name made lowercase.
    number_4bqty = models.IntegerField(db_column='4BQty', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    reportno = models.CharField(db_column='reportNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    repstatus = models.CharField(db_column='repStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    uploadfile = models.CharField(db_column='uploadFile', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rmpstatus'


class Role(models.Model):
    role_rolecode = models.CharField(primary_key=True, max_length=50)
    role_rolename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'role'


class RoleRights(models.Model):
    rr_rolecode = models.OneToOneField(Role, models.DO_NOTHING, db_column='rr_rolecode', primary_key=True)
    rr_modulecode = models.ForeignKey(Module, models.DO_NOTHING, db_column='rr_modulecode')
    rr_create = models.CharField(max_length=3)
    rr_edit = models.CharField(max_length=3)
    rr_delete = models.CharField(max_length=3)
    rr_view = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'role_rights'
        unique_together = (('rr_rolecode', 'rr_modulecode'),)


class SensormanagementMaster(models.Model):
    sitelocation = models.CharField(db_column='siteLocation', max_length=255)  # Field name made lowercase.
    room = models.CharField(max_length=255)
    mastername = models.CharField(db_column='masterName', max_length=255)  # Field name made lowercase.
    installationdatetime = models.DateTimeField(db_column='installationDatetime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sensorManagement_master'


class SensormanagementSensor(models.Model):
    room = models.CharField(max_length=255)
    sensortype = models.CharField(db_column='sensorType', max_length=255)  # Field name made lowercase.
    compressor = models.CharField(max_length=255)
    installationdatetime = models.DateTimeField(db_column='installationDatetime')  # Field name made lowercase.
    masterid = models.IntegerField(db_column='masterId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sensorManagement_sensor'


class Shippingbilldetails(models.Model):
    invoiceno = models.CharField(db_column='invoiceNo', primary_key=True, max_length=45)  # Field name made lowercase.
    shippingbilldate = models.DateField(db_column='shippingBillDate')  # Field name made lowercase.
    shippingbillno = models.PositiveIntegerField(db_column='shippingBillNo')  # Field name made lowercase.
    exchangecur = models.CharField(db_column='exchangeCur', max_length=5, blank=True, null=True)  # Field name made lowercase.
    exchangerate = models.FloatField(db_column='exchangeRate')  # Field name made lowercase.
    fobinr = models.FloatField(db_column='fobINR')  # Field name made lowercase.
    fobforex = models.FloatField(db_column='fobForEx')  # Field name made lowercase.
    dutydrawback = models.FloatField(db_column='dutyDrawback')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippingBillDetails'


class Shippinglinesschedule(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shipline = models.CharField(db_column='ShipLine', max_length=45)  # Field name made lowercase.
    voyageno = models.CharField(db_column='voyageNo', max_length=15)  # Field name made lowercase.
    eta_etd_1_0_field = models.CharField(db_column='ETA/ETD(1/0)', max_length=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    port = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'shippingLinesSchedule'


class Shippingline(models.Model):
    shippinglinecode = models.CharField(db_column='shippingLineCode', primary_key=True, max_length=11, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    shippinglinename = models.CharField(db_column='shippingLineName', max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    trackurl = models.CharField(db_column='TrackURL', max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=120, db_collation='utf8_unicode_ci', blank=True, null=True)
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    mobilesales = models.CharField(db_column='mobileSales', max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    mobileaccts = models.CharField(db_column='mobileACCTS', max_length=10, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    emailaccts = models.CharField(db_column='emailACCTS', max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    emailsales = models.CharField(db_column='emailSALES', max_length=45, db_collation='utf8_unicode_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shippingline'


class Site(models.Model):
    siteid = models.AutoField(db_column='siteId', unique=True)  # Field name made lowercase.
    sitecode = models.CharField(max_length=7, blank=True, null=True)
    sitename = models.CharField(db_column='siteName', primary_key=True, max_length=12, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    siteremarks = models.CharField(max_length=20)
    siteadd = models.CharField(max_length=30)
    fssai_no = models.CharField(db_column='FSSAI_NO', max_length=25)  # Field name made lowercase.
    fssai_validity = models.DateField(db_column='FSSAI_Validity')  # Field name made lowercase.
    fssai_doclink = models.CharField(db_column='Fssai_DocLink', max_length=40)  # Field name made lowercase.
    globalgap_no = models.CharField(db_column='GlobalGap_No', max_length=25)  # Field name made lowercase.
    globalgap_validity = models.DateField(db_column='GlobalGap_Validity')  # Field name made lowercase.
    globalgap_doclink = models.CharField(db_column='GlobalGap_DocLink', max_length=40)  # Field name made lowercase.
    brc_no = models.CharField(db_column='BRC_NO', max_length=25)  # Field name made lowercase.
    brc_validity = models.DateField(db_column='BRC_Validity')  # Field name made lowercase.
    brc_doclink = models.CharField(db_column='BRC_DocLink', max_length=40)  # Field name made lowercase.
    apeda_phno = models.CharField(db_column='APEDA_PHNO', max_length=25)  # Field name made lowercase.
    apedaph_validity = models.DateField(db_column='ApedaPH_Validity')  # Field name made lowercase.
    apedaph_doclink = models.CharField(db_column='ApedaPH_DocLink', max_length=40)  # Field name made lowercase.
    agmarkno = models.CharField(db_column='AgmarkNo', max_length=25)  # Field name made lowercase.
    agmark_validity = models.DateField(db_column='Agmark_Validity')  # Field name made lowercase.
    agmark_doclink = models.CharField(db_column='Agmark_Doclink', max_length=40)  # Field name made lowercase.
    gst_lutno = models.CharField(db_column='GST_LUTNo', max_length=25)  # Field name made lowercase.
    gst_lutvalidity = models.DateField(db_column='GST_LUTValidity')  # Field name made lowercase.
    gst_lutdoclink = models.IntegerField(db_column='GST_LUTDocLink')  # Field name made lowercase.
    stuffpermission = models.CharField(db_column='StuffPermission', max_length=120)  # Field name made lowercase.
    stuffper_validity = models.DateField(db_column='StuffPer_Validity')  # Field name made lowercase.
    stuffperdoclink = models.CharField(db_column='StuffPerDocLink', max_length=40)  # Field name made lowercase.
    siteinsuranceno = models.CharField(db_column='SiteInsuranceNo', max_length=25)  # Field name made lowercase.
    siteinsvalidity = models.DateField(db_column='SiteInsValidity')  # Field name made lowercase.
    siteinsdoclink = models.CharField(db_column='SiteInsDocLink', max_length=40)  # Field name made lowercase.
    siteleaseno = models.IntegerField(db_column='SiteLeaseNo')  # Field name made lowercase.
    sitelease_validity = models.DateField(db_column='SiteLease_Validity')  # Field name made lowercase.
    sitelease_doclink = models.IntegerField(db_column='SiteLease_DocLink')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site'


class States(models.Model):
    statecode = models.AutoField(db_column='stateCode', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='stateName', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'states'


class Stationstatus(models.Model):
    stationid = models.IntegerField(db_column='stationID', primary_key=True)  # Field name made lowercase.
    lineno = models.IntegerField(db_column='lineNo', blank=True, null=True)  # Field name made lowercase.
    flag_updated = models.IntegerField(blank=True, null=True)
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stationstatus'


class SystemUsers(models.Model):
    u_userid = models.AutoField(primary_key=True)
    u_username = models.CharField(max_length=100)
    u_password = models.CharField(max_length=255, blank=True, null=True)
    u_rolecode = models.ForeignKey(Role, models.DO_NOTHING, db_column='u_rolecode')

    class Meta:
        managed = False
        db_table = 'system_users'


class Timezones(models.Model):
    countrycode = models.IntegerField(db_column='countryCode', primary_key=True)  # Field name made lowercase.
    timediff = models.DecimalField(db_column='timeDiff', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timezones'


class Transhipmentport(models.Model):
    id = models.AutoField()
    transhipmentportname = models.CharField(db_column='transhipmentPortName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transhipmentPort'


class Transporter(models.Model):
    tptcode = models.IntegerField(db_column='tptCode', primary_key=True)  # Field name made lowercase.
    tptname = models.CharField(db_column='tptName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tptaddress = models.CharField(db_column='tptAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    citycode = models.IntegerField(db_column='cityCode', blank=True, null=True)  # Field name made lowercase.
    statecode = models.IntegerField(db_column='stateCode', blank=True, null=True)  # Field name made lowercase.
    mobileno1 = models.CharField(db_column='mobileNo1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mobileno2 = models.CharField(db_column='mobileNo2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gstin = models.CharField(db_column='GSTIN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.IntegerField(db_column='bankCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transporter'


class Units(models.Model):
    unitid = models.AutoField(primary_key=True)
    unitcode = models.CharField(db_column='unitCode', unique=True, max_length=6)  # Field name made lowercase.
    unitname = models.CharField(db_column='unitName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=6)
    childunitqty = models.IntegerField(db_column='childUnitQty')  # Field name made lowercase.
    childunitcode = models.CharField(db_column='childUnitCode', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'units'


class UsermanagementEmployeedata(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True)  # Field name made lowercase.
    empcode = models.CharField(db_column='empCode', max_length=8)  # Field name made lowercase.
    empname = models.CharField(db_column='empName', max_length=45)  # Field name made lowercase.
    team = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    mobile1 = models.BigIntegerField()
    mobile2 = models.BigIntegerField(blank=True, null=True)
    bankacno = models.CharField(db_column='bankACno', max_length=15, blank=True, null=True)  # Field name made lowercase.
    bankifsc = models.CharField(db_column='bankIFSC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    acholdername = models.CharField(db_column='AcHolderName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pan = models.CharField(db_column='PAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    aadhaar = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.DateField(db_column='joiningDate', blank=True, null=True)  # Field name made lowercase.
    eduqual = models.CharField(db_column='eduQual', max_length=45, blank=True, null=True)  # Field name made lowercase.
    experience = models.IntegerField(blank=True, null=True)
    maritalstatus = models.CharField(db_column='maritalStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dependants = models.CharField(max_length=45, blank=True, null=True)
    refname = models.CharField(db_column='refName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    refaddress = models.CharField(db_column='refAddress', max_length=120, blank=True, null=True)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sifacode = models.IntegerField(db_column='SIFACode', blank=True, null=True)  # Field name made lowercase.
    accesstype = models.IntegerField(db_column='accessType', blank=True, null=True)  # Field name made lowercase.
    sifaserialnumber = models.IntegerField(db_column='SIFASerialNumber', blank=True, null=True)  # Field name made lowercase.
    empshortcode = models.CharField(db_column='empShortCode', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userManagement_employeedata'


class UsermanagementFeuser(models.Model):
    username = models.CharField(primary_key=True, max_length=11)
    password = models.CharField(max_length=255)
    empcode = models.CharField(db_column='empCode', unique=True, max_length=8, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    team1 = models.CharField(max_length=3, blank=True, null=True)
    team2 = models.CharField(max_length=3, blank=True, null=True)
    team3 = models.CharField(max_length=3, blank=True, null=True)
    team4 = models.CharField(max_length=3, blank=True, null=True)
    team5 = models.CharField(max_length=3, blank=True, null=True)
    team6 = models.CharField(max_length=3, blank=True, null=True)
    team7 = models.CharField(max_length=3, blank=True, null=True)
    team8 = models.CharField(max_length=3, blank=True, null=True)
    team9 = models.CharField(max_length=3, blank=True, null=True)
    team10 = models.CharField(max_length=3, blank=True, null=True)
    team11 = models.CharField(max_length=3, blank=True, null=True)
    team12 = models.CharField(max_length=3, blank=True, null=True)
    team13 = models.CharField(max_length=3, blank=True, null=True)
    team14 = models.CharField(max_length=3, blank=True, null=True)
    team15 = models.CharField(max_length=3, blank=True, null=True)
    act_status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'userManagement_feuser'


class UsermanagementSites(models.Model):
    siteid = models.AutoField(db_column='siteId', primary_key=True)  # Field name made lowercase.
    sitecode = models.CharField(max_length=6)
    sitename = models.CharField(db_column='siteName', unique=True, max_length=12, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    siteremarks = models.CharField(max_length=20)
    siteadd = models.CharField(max_length=30)
    fssai_no = models.CharField(db_column='FSSAI_NO', max_length=25)  # Field name made lowercase.
    fssai_validity = models.DateField(db_column='FSSAI_Validity')  # Field name made lowercase.
    fssai_doclink = models.CharField(db_column='Fssai_DocLink', max_length=40)  # Field name made lowercase.
    globalgap_no = models.CharField(db_column='GlobalGap_No', max_length=25)  # Field name made lowercase.
    globalgap_validity = models.DateField(db_column='GlobalGap_Validity')  # Field name made lowercase.
    globalgap_doclink = models.CharField(db_column='GlobalGap_DocLink', max_length=40)  # Field name made lowercase.
    brc_no = models.CharField(db_column='BRC_NO', max_length=25)  # Field name made lowercase.
    brc_validity = models.DateField(db_column='BRC_Validity')  # Field name made lowercase.
    brc_doclink = models.CharField(db_column='BRC_DocLink', max_length=40)  # Field name made lowercase.
    apeda_phno = models.CharField(db_column='APEDA_PHNO', max_length=25)  # Field name made lowercase.
    apedaph_validity = models.DateField(db_column='ApedaPH_Validity')  # Field name made lowercase.
    apedaph_doclink = models.CharField(db_column='ApedaPH_DocLink', max_length=40)  # Field name made lowercase.
    agmarkno = models.CharField(db_column='AgmarkNo', max_length=25)  # Field name made lowercase.
    agmark_validity = models.DateField(db_column='Agmark_Validity')  # Field name made lowercase.
    agmark_doclink = models.CharField(db_column='Agmark_Doclink', max_length=40)  # Field name made lowercase.
    gst_lutno = models.CharField(db_column='GST_LUTNo', max_length=25)  # Field name made lowercase.
    gst_lutvalidity = models.DateField(db_column='GST_LUTValidity')  # Field name made lowercase.
    gst_lutdoclink = models.IntegerField(db_column='GST_LUTDocLink')  # Field name made lowercase.
    stuffpermission = models.CharField(db_column='StuffPermission', max_length=40)  # Field name made lowercase.
    stuffper_validity = models.DateField(db_column='StuffPer_Validity')  # Field name made lowercase.
    stuffperdoclink = models.CharField(db_column='StuffPerDocLink', max_length=40)  # Field name made lowercase.
    siteinsuranceno = models.CharField(db_column='SiteInsuranceNo', max_length=25)  # Field name made lowercase.
    siteinsvalidity = models.DateField(db_column='SiteInsValidity')  # Field name made lowercase.
    siteinsdoclink = models.CharField(db_column='SiteInsDocLink', max_length=40)  # Field name made lowercase.
    siteleaseno = models.IntegerField(db_column='SiteLeaseNo')  # Field name made lowercase.
    sitelease_validity = models.DateField(db_column='SiteLease_Validity')  # Field name made lowercase.
    sitelease_doclink = models.IntegerField(db_column='SiteLease_DocLink')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userManagement_sites'


class UsermanagementTeam(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'userManagement_team'


class Users(models.Model):
    loginid = models.CharField(db_column='loginID', primary_key=True, max_length=11)  # Field name made lowercase.
    empcode = models.IntegerField(db_column='empCode')  # Field name made lowercase.
    password = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'users'


class Variety(models.Model):
    varietyid = models.AutoField(db_column='varietyId', primary_key=True)  # Field name made lowercase.
    varietycode = models.CharField(db_column='varietyCode', unique=True, max_length=7)  # Field name made lowercase.
    variety = models.CharField(max_length=40, blank=True, null=True)
    cropcode = models.CharField(db_column='cropCode', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variety'


class Vehicles(models.Model):
    vehcode = models.CharField(db_column='Vehcode', primary_key=True, max_length=10, db_collation='utf8_unicode_ci')  # Field name made lowercase.
    vshort_name = models.CharField(db_column='Vshort_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    vregno = models.IntegerField(db_column='VregNo', blank=True, null=True)  # Field name made lowercase.
    make = models.CharField(max_length=45, blank=True, null=True)
    bodytype = models.CharField(db_column='BodyType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mfgyear = models.IntegerField(blank=True, null=True)
    chasisno = models.CharField(db_column='chasisNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    engineno = models.CharField(db_column='engineNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    policyno = models.CharField(db_column='policyNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idv = models.CharField(db_column='IDV', max_length=45, blank=True, null=True)  # Field name made lowercase.
    policyduedate = models.DateField(db_column='policyDueDate', blank=True, null=True)  # Field name made lowercase.
    permitno = models.CharField(db_column='permitNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    validupto = models.DateField(blank=True, null=True)
    authvalidity = models.DateField(db_column='authValidity', blank=True, null=True)  # Field name made lowercase.
    fitnessvalidity = models.DateField(db_column='fitnessValidity', blank=True, null=True)  # Field name made lowercase.
    counterdetails = models.IntegerField(db_column='counterDetails', blank=True, null=True)  # Field name made lowercase.
    ownercode = models.IntegerField(db_column='ownerCode', blank=True, null=True)  # Field name made lowercase.
    vehicletype = models.IntegerField(db_column='vehicleType', blank=True, null=True)  # Field name made lowercase.
    staxvalidity = models.DateField(db_column='STaxValidity', blank=True, null=True)  # Field name made lowercase.
    cftcapacity = models.CharField(db_column='CFTcapacity', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hypothication = models.CharField(max_length=45, blank=True, null=True)
    contractfrom = models.DateField(db_column='contractFrom', blank=True, null=True)  # Field name made lowercase.
    contractto = models.DateField(db_column='contractTo', blank=True, null=True)  # Field name made lowercase.
    payloadwt = models.DecimalField(db_column='PayloadWt', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hometaxvalidity = models.DateField(db_column='homeTaxValidity', blank=True, null=True)  # Field name made lowercase.
    ptaxvalidity = models.DateField(db_column='PTaxValidity', blank=True, null=True)  # Field name made lowercase.
    envtaxvalidity = models.DateField(db_column='envTaxValidity', blank=True, null=True)  # Field name made lowercase.
    insurancecompany = models.CharField(db_column='insuranceCompany', max_length=45, blank=True, null=True)  # Field name made lowercase.
    containersize = models.IntegerField(db_column='containerSize', blank=True, null=True)  # Field name made lowercase.
    laddenwt = models.DecimalField(db_column='laddenWt', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicles'


class Vesselschedule(models.Model):
    shippingline = models.CharField(db_column='shippingLine', max_length=10)  # Field name made lowercase.
    serviceshipping = models.CharField(db_column='serviceShipping', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vesselname = models.CharField(db_column='vesselName', max_length=20)  # Field name made lowercase.
    voyageno = models.CharField(db_column='voyageNo', max_length=20)  # Field name made lowercase.
    transhipmentport = models.CharField(db_column='transhipmentPort', max_length=45, blank=True, null=True)  # Field name made lowercase.
    eta_jnpt = models.DateTimeField(db_column='ETA_JNPT', blank=True, null=True)  # Field name made lowercase.
    etd_jnpt = models.DateTimeField(db_column='ETD_JNPT', blank=True, null=True)  # Field name made lowercase.
    destinationporteta = models.DateTimeField(db_column='destinationPortETA', blank=True, null=True)  # Field name made lowercase.
    reviseddestinationeta = models.DateTimeField(db_column='revisedDestinationETA', blank=True, null=True)  # Field name made lowercase.
    transhipmentporteta = models.DateTimeField(db_column='transhipmentPortETA', blank=True, null=True)  # Field name made lowercase.
    transhipmentportetd = models.DateTimeField(db_column='transhipmentPortETD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vesselSchedule'


class Wastage(models.Model):
    srno = models.AutoField(primary_key=True)
    controlno = models.IntegerField(db_column='controlNo')  # Field name made lowercase.
    berrybunch = models.IntegerField(db_column='berryBunch', blank=True, null=True)  # Field name made lowercase.
    cratetypecode = models.IntegerField(db_column='crateTypeCode', blank=True, null=True)  # Field name made lowercase.
    cratesqty = models.IntegerField(db_column='cratesQty', blank=True, null=True)  # Field name made lowercase.
    grosswt = models.DecimalField(db_column='grossWt', unique=True, max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    emptywt = models.DecimalField(db_column='emptyWt', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    netwt = models.DecimalField(db_column='netWt', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    stationid = models.IntegerField(db_column='stationID', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    wtdate = models.CharField(db_column='wtDate', max_length=12, blank=True, null=True)  # Field name made lowercase.
    wttime = models.CharField(db_column='wtTime', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wastage'


class XCustomportcode(models.Model):
    portcode = models.CharField(db_column='portCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x_customPortCode'


class Ztempmrj(models.Model):
    srno = models.IntegerField()
    tempsr1d = models.DecimalField(max_digits=8, decimal_places=2)
    tempsr2d = models.DecimalField(max_digits=8, decimal_places=2)
    tempsr3d = models.DecimalField(max_digits=8, decimal_places=2)
    tempsr4d = models.DecimalField(max_digits=8, decimal_places=2)
    tempsr5d = models.DecimalField(max_digits=8, decimal_places=2)
    humid1r = models.DecimalField(max_digits=8, decimal_places=2)
    humid2r = models.DecimalField(max_digits=8, decimal_places=2)
    humid3r = models.DecimalField(max_digits=8, decimal_places=2)
    humid4r = models.DecimalField(max_digits=8, decimal_places=2)
    humid5r = models.DecimalField(max_digits=8, decimal_places=2)
    tempdate = models.DateField()
    temptime = models.TimeField()
    vtimestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ztempmrj'
