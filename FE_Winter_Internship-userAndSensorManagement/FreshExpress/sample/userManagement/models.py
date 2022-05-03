from django.db import models

# Create your models here.


class Team(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)


class Employee(models.Model):
    # Field name made lowercase.
    empid = models.AutoField(db_column='empId', primary_key=True)
    # Field name made lowercase.
    empcode = models.CharField(db_column='empCode', max_length=8)
    # Field name made lowercase.
    empname = models.CharField(db_column='empName', max_length=45)
    # Field name made lowercase.
    empemail = models.CharField(
        db_column='empEmail', max_length=45, blank=True, null=True)
    team = models.CharField(max_length=30, blank=True, null=True)
    site = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    mobile1 = models.BigIntegerField()
    mobile2 = models.BigIntegerField(blank=True, null=True)
    # Field name made lowercase.
    bankacno = models.CharField(
        db_column='bankACno', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    bankifsc = models.CharField(
        db_column='bankIFSC', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    acholdername = models.CharField(
        db_column='AcHolderName', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    pan = models.CharField(
        db_column='PAN', max_length=10, blank=True, null=True)
    aadhaar = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)
    # Field name made lowercase.
    joiningdate = models.DateField(
        db_column='joiningDate', blank=True, null=True)
    # Field name made lowercase.
    eduqual = models.CharField(
        db_column='eduQual', max_length=45, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    maritalstatus = models.CharField(
        db_column='maritalStatus', max_length=10, blank=True, null=True)
    dependants = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    refname = models.CharField(
        db_column='refName', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    refaddress = models.CharField(
        db_column='refAddress', max_length=120, blank=True, null=True)
    # Field name made lowercase.
    rfid = models.CharField(
        db_column='RFID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    sifacode = models.IntegerField(db_column='SIFACode', blank=True, null=True)
    # Field name made lowercase.
    accesstype = models.IntegerField(
        db_column='accessType', blank=True, null=True)
    # Field name made lowercase.
    sifaserialnumber = models.IntegerField(
        db_column='SIFASerialNumber', blank=True, null=True)
    # Field name made lowercase.
    empshortcode = models.CharField(
        db_column='empShortCode', max_length=4, blank=True, null=True)
    actstatus = models.CharField(
        db_column='actstatus', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    usercreated = models.IntegerField(
        db_column='userCreated', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


# class EmployeeData(models.Model):
#     # Field name made lowercase.
#     empid = models.AutoField(db_column='empId', primary_key=True)
#     # Field name made lowercase.
#     empcode = models.CharField(db_column='empCode', max_length=8)
#     # Field name made lowercase.
#     empname = models.CharField(db_column='empName', max_length=45)
#     team = models.CharField(max_length=30, blank=True, null=True)
#     site = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=120, blank=True, null=True)
#     pincode = models.IntegerField(blank=True, null=True)
#     mobile1 = models.BigIntegerField()
#     mobile2 = models.BigIntegerField(blank=True, null=True)
#     # Field name made lowercase.
#     bankacno = models.CharField(
#         db_column='bankACno', max_length=15, blank=True, null=True)
#     # Field name made lowercase.
#     bankifsc = models.CharField(
#         db_column='bankIFSC', max_length=12, blank=True, null=True)
#     # Field name made lowercase.
#     acholdername = models.CharField(
#         db_column='AcHolderName', max_length=45, blank=True, null=True)
#     # Field name made lowercase.
#     pan = models.CharField(
#         db_column='PAN', max_length=10, blank=True, null=True)
#     aadhaar = models.CharField(max_length=12, blank=True, null=True)
#     gender = models.CharField(max_length=10, blank=True, null=True)
#     # Field name made lowercase.
#     dob = models.DateField(db_column='DOB', blank=True, null=True)
#     # Field name made lowercase.
#     joiningdate = models.DateField(
#         db_column='joiningDate', blank=True, null=True)
#     # Field name made lowercase.
#     eduqual = models.CharField(
#         db_column='eduQual', max_length=45, blank=True, null=True)
#     experience = models.IntegerField(blank=True, null=True)
#     # Field name made lowercase.
#     maritalstatus = models.CharField(
#         db_column='maritalStatus', max_length=10, blank=True, null=True)
#     dependants = models.CharField(max_length=45, blank=True, null=True)
#     # Field name made lowercase.
#     refname = models.CharField(
#         db_column='refName', max_length=45, blank=True, null=True)
#     # Field name made lowercase.
#     refaddress = models.CharField(
#         db_column='refAddress', max_length=120, blank=True, null=True)
#     # Field name made lowercase.
#     rfid = models.CharField(
#         db_column='RFID', max_length=15, blank=True, null=True)
#     # Field name made lowercase.
#     sifacode = models.IntegerField(db_column='SIFACode', blank=True, null=True)
#     # Field name made lowercase.
#     accesstype = models.IntegerField(
#         db_column='accessType', blank=True, null=True)
#     # Field name made lowercase.
#     sifaserialnumber = models.IntegerField(
#         db_column='SIFASerialNumber', blank=True, null=True)
#     # Field name made lowercase.
#     empshortcode = models.CharField(
#         db_column='empShortCode', max_length=4, blank=True, null=True)


class FeUser(models.Model):
    username = models.CharField(primary_key=True, max_length=11)
    password = models.CharField(max_length=255)
    # Field name made lowercase.
    empcode = models.CharField(
        db_column='empCode', unique=True, max_length=8, blank=True, null=True)
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
    act_status = models.CharField(max_length=10)


# class Sites(models.Model):
#     # Field name made lowercase.
#     siteid = models.AutoField(db_column='siteId', primary_key=True)
#     sitecode = models.CharField(max_length=6)
#     # Field name made lowercase.
#     sitename = models.CharField(
#         db_column='siteName', unique=True, max_length=12, db_collation='utf8_unicode_ci')
#     siteremarks = models.CharField(max_length=20)
#     siteadd = models.CharField(max_length=30)
#     # Field name made lowercase.
#     fssai_no = models.CharField(db_column='FSSAI_NO', max_length=25)
#     # Field name made lowercase.
#     fssai_validity = models.DateField(db_column='FSSAI_Validity')
#     # Field name made lowercase.
#     fssai_doclink = models.CharField(db_column='Fssai_DocLink', max_length=40)
#     # Field name made lowercase.
#     globalgap_no = models.CharField(db_column='GlobalGap_No', max_length=25)
#     # Field name made lowercase.
#     globalgap_validity = models.DateField(db_column='GlobalGap_Validity')
#     # Field name made lowercase.
#     globalgap_doclink = models.CharField(
#         db_column='GlobalGap_DocLink', max_length=40)
#     # Field name made lowercase.
#     brc_no = models.CharField(db_column='BRC_NO', max_length=25)
#     # Field name made lowercase.
#     brc_validity = models.DateField(db_column='BRC_Validity')
#     # Field name made lowercase.
#     brc_doclink = models.CharField(db_column='BRC_DocLink', max_length=40)
#     # Field name made lowercase.
#     apeda_phno = models.CharField(db_column='APEDA_PHNO', max_length=25)
#     # Field name made lowercase.
#     apedaph_validity = models.DateField(db_column='ApedaPH_Validity')
#     # Field name made lowercase.
#     apedaph_doclink = models.CharField(
#         db_column='ApedaPH_DocLink', max_length=40)
#     # Field name made lowercase.
#     agmarkno = models.CharField(db_column='AgmarkNo', max_length=25)
#     # Field name made lowercase.
#     agmark_validity = models.DateField(db_column='Agmark_Validity')
#     # Field name made lowercase.
#     agmark_doclink = models.CharField(
#         db_column='Agmark_Doclink', max_length=40)
#     # Field name made lowercase.
#     gst_lutno = models.CharField(db_column='GST_LUTNo', max_length=25)
#     # Field name made lowercase.
#     gst_lutvalidity = models.DateField(db_column='GST_LUTValidity')
#     # Field name made lowercase.
#     gst_lutdoclink = models.IntegerField(db_column='GST_LUTDocLink')
#     # Field name made lowercase.
#     stuffpermission = models.CharField(
#         db_column='StuffPermission', max_length=40)
#     # Field name made lowercase.
#     stuffper_validity = models.DateField(db_column='StuffPer_Validity')
#     # Field name made lowercase.
#     stuffperdoclink = models.CharField(
#         db_column='StuffPerDocLink', max_length=40)
#     # Field name made lowercase.
#     siteinsuranceno = models.CharField(
#         db_column='SiteInsuranceNo', max_length=25)
#     # Field name made lowercase.
#     siteinsvalidity = models.DateField(db_column='SiteInsValidity')
#     # Field name made lowercase.
#     siteinsdoclink = models.CharField(
#         db_column='SiteInsDocLink', max_length=40)
#     # Field name made lowercase.
#     siteleaseno = models.IntegerField(db_column='SiteLeaseNo')
#     # Field name made lowercase.
#     sitelease_validity = models.DateField(db_column='SiteLease_Validity')
#     # Field name made lowercase.
#     sitelease_doclink = models.IntegerField(db_column='SiteLease_DocLink')


class Site(models.Model):
    # Field name made lowercase.
    siteid = models.IntegerField(db_column='siteId', unique=True)
    sitecode = models.CharField(max_length=6)
    # Field name made lowercase.
    sitename = models.CharField(
        db_column='siteName', primary_key=True, max_length=12, db_collation='utf8_unicode_ci')
    siteremarks = models.CharField(max_length=20)
    siteadd = models.CharField(max_length=30)
    # Field name made lowercase.
    fssai_no = models.CharField(db_column='FSSAI_NO', max_length=25)
    # Field name made lowercase.
    fssai_validity = models.DateField(db_column='FSSAI_Validity')
    # Field name made lowercase.
    fssai_doclink = models.CharField(db_column='Fssai_DocLink', max_length=40)
    # Field name made lowercase.
    globalgap_no = models.CharField(db_column='GlobalGap_No', max_length=25)
    # Field name made lowercase.
    globalgap_validity = models.DateField(db_column='GlobalGap_Validity')
    # Field name made lowercase.
    globalgap_doclink = models.CharField(
        db_column='GlobalGap_DocLink', max_length=40)
    # Field name made lowercase.
    brc_no = models.CharField(db_column='BRC_NO', max_length=25)
    # Field name made lowercase.
    brc_validity = models.DateField(db_column='BRC_Validity')
    # Field name made lowercase.
    brc_doclink = models.CharField(db_column='BRC_DocLink', max_length=40)
    # Field name made lowercase.
    apeda_phno = models.CharField(db_column='APEDA_PHNO', max_length=25)
    # Field name made lowercase.
    apedaph_validity = models.DateField(db_column='ApedaPH_Validity')
    # Field name made lowercase.
    apedaph_doclink = models.CharField(
        db_column='ApedaPH_DocLink', max_length=40)
    # Field name made lowercase.
    agmarkno = models.CharField(db_column='AgmarkNo', max_length=25)
    # Field name made lowercase.
    agmark_validity = models.DateField(db_column='Agmark_Validity')
    # Field name made lowercase.
    agmark_doclink = models.CharField(
        db_column='Agmark_Doclink', max_length=40)
    # Field name made lowercase.
    gst_lutno = models.CharField(db_column='GST_LUTNo', max_length=25)
    # Field name made lowercase.
    gst_lutvalidity = models.DateField(db_column='GST_LUTValidity')
    # Field name made lowercase.
    gst_lutdoclink = models.IntegerField(db_column='GST_LUTDocLink')
    # Field name made lowercase.
    stuffpermission = models.CharField(
        db_column='StuffPermission', max_length=40)
    # Field name made lowercase.
    stuffper_validity = models.DateField(db_column='StuffPer_Validity')
    # Field name made lowercase.
    stuffperdoclink = models.CharField(
        db_column='StuffPerDocLink', max_length=40)
    # Field name made lowercase.
    siteinsuranceno = models.CharField(
        db_column='SiteInsuranceNo', max_length=25)
    # Field name made lowercase.
    siteinsvalidity = models.DateField(db_column='SiteInsValidity')
    # Field name made lowercase.
    siteinsdoclink = models.CharField(
        db_column='SiteInsDocLink', max_length=40)
    # Field name made lowercase.
    siteleaseno = models.IntegerField(db_column='SiteLeaseNo')
    # Field name made lowercase.
    sitelease_validity = models.DateField(db_column='SiteLease_Validity')
    # Field name made lowercase.
    sitelease_doclink = models.IntegerField(db_column='SiteLease_DocLink')

    class Meta:
        managed = False
        db_table = 'site'
