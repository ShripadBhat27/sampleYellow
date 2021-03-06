# Generated by Django 4.0 on 2022-01-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('empid', models.AutoField(db_column='empId', primary_key=True, serialize=False)),
                ('empcode', models.CharField(db_column='empCode', max_length=8)),
                ('empname', models.CharField(db_column='empName', max_length=45)),
                ('team', models.CharField(blank=True, max_length=30, null=True)),
                ('site', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('mobile1', models.BigIntegerField()),
                ('mobile2', models.BigIntegerField(blank=True, null=True)),
                ('bankacno', models.CharField(blank=True, db_column='bankACno', max_length=15, null=True)),
                ('bankifsc', models.CharField(blank=True, db_column='bankIFSC', max_length=12, null=True)),
                ('acholdername', models.CharField(blank=True, db_column='AcHolderName', max_length=45, null=True)),
                ('pan', models.CharField(blank=True, db_column='PAN', max_length=10, null=True)),
                ('aadhaar', models.CharField(blank=True, max_length=12, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('joiningdate', models.DateField(blank=True, db_column='joiningDate', null=True)),
                ('eduqual', models.CharField(blank=True, db_column='eduQual', max_length=45, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('maritalstatus', models.CharField(blank=True, db_column='maritalStatus', max_length=10, null=True)),
                ('dependants', models.CharField(blank=True, max_length=45, null=True)),
                ('refname', models.CharField(blank=True, db_column='refName', max_length=45, null=True)),
                ('refaddress', models.CharField(blank=True, db_column='refAddress', max_length=120, null=True)),
                ('rfid', models.CharField(blank=True, db_column='RFID', max_length=15, null=True)),
                ('sifacode', models.IntegerField(blank=True, db_column='SIFACode', null=True)),
                ('accesstype', models.IntegerField(blank=True, db_column='accessType', null=True)),
                ('sifaserialnumber', models.IntegerField(blank=True, db_column='SIFASerialNumber', null=True)),
                ('empshortcode', models.CharField(blank=True, db_column='empShortCode', max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeUser',
            fields=[
                ('username', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('empcode', models.CharField(blank=True, db_column='empCode', max_length=8, null=True, unique=True)),
                ('team1', models.CharField(blank=True, max_length=3, null=True)),
                ('team2', models.CharField(blank=True, max_length=3, null=True)),
                ('team3', models.CharField(blank=True, max_length=3, null=True)),
                ('team4', models.CharField(blank=True, max_length=3, null=True)),
                ('team5', models.CharField(blank=True, max_length=3, null=True)),
                ('team6', models.CharField(blank=True, max_length=3, null=True)),
                ('team7', models.CharField(blank=True, max_length=3, null=True)),
                ('team8', models.CharField(blank=True, max_length=3, null=True)),
                ('team9', models.CharField(blank=True, max_length=3, null=True)),
                ('team10', models.CharField(blank=True, max_length=3, null=True)),
                ('act_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('siteid', models.AutoField(db_column='siteId', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(max_length=6)),
                ('sitename', models.CharField(db_collation='utf8_unicode_ci', db_column='siteName', max_length=12, unique=True)),
                ('siteremarks', models.CharField(max_length=20)),
                ('siteadd', models.CharField(max_length=30)),
                ('fssai_no', models.CharField(db_column='FSSAI_NO', max_length=25)),
                ('fssai_validity', models.DateField(db_column='FSSAI_Validity')),
                ('fssai_doclink', models.CharField(db_column='Fssai_DocLink', max_length=40)),
                ('globalgap_no', models.CharField(db_column='GlobalGap_No', max_length=25)),
                ('globalgap_validity', models.DateField(db_column='GlobalGap_Validity')),
                ('globalgap_doclink', models.CharField(db_column='GlobalGap_DocLink', max_length=40)),
                ('brc_no', models.CharField(db_column='BRC_NO', max_length=25)),
                ('brc_validity', models.DateField(db_column='BRC_Validity')),
                ('brc_doclink', models.CharField(db_column='BRC_DocLink', max_length=40)),
                ('apeda_phno', models.CharField(db_column='APEDA_PHNO', max_length=25)),
                ('apedaph_validity', models.DateField(db_column='ApedaPH_Validity')),
                ('apedaph_doclink', models.CharField(db_column='ApedaPH_DocLink', max_length=40)),
                ('agmarkno', models.CharField(db_column='AgmarkNo', max_length=25)),
                ('agmark_validity', models.DateField(db_column='Agmark_Validity')),
                ('agmark_doclink', models.CharField(db_column='Agmark_Doclink', max_length=40)),
                ('gst_lutno', models.CharField(db_column='GST_LUTNo', max_length=25)),
                ('gst_lutvalidity', models.DateField(db_column='GST_LUTValidity')),
                ('gst_lutdoclink', models.IntegerField(db_column='GST_LUTDocLink')),
                ('stuffpermission', models.CharField(db_column='StuffPermission', max_length=40)),
                ('stuffper_validity', models.DateField(db_column='StuffPer_Validity')),
                ('stuffperdoclink', models.CharField(db_column='StuffPerDocLink', max_length=40)),
                ('siteinsuranceno', models.CharField(db_column='SiteInsuranceNo', max_length=25)),
                ('siteinsvalidity', models.DateField(db_column='SiteInsValidity')),
                ('siteinsdoclink', models.CharField(db_column='SiteInsDocLink', max_length=40)),
                ('siteleaseno', models.IntegerField(db_column='SiteLeaseNo')),
                ('sitelease_validity', models.DateField(db_column='SiteLease_Validity')),
                ('sitelease_doclink', models.IntegerField(db_column='SiteLease_DocLink')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
