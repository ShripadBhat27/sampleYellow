from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
import re
from sample.settings import MESSAGE_STORAGE
from django.contrib.auth.decorators import login_required
from Login.decorators import allowed_users
from django.contrib.auth.models import User
from .models import Team, Employee, Site
from Login.models import LoginAppuser
from django.template import loader


@login_required
@allowed_users(allowed_teams=['team6'])
def employees(request):
    employees = Employee.objects.all().order_by('empcode')
    sites = Site.objects.all()
    template = loader.get_template('userManagement/employees.html')
    context = {
        'employees': employees,
        'sites': sites,
    }
    return HttpResponse(template.render(context, request))


@login_required
@allowed_users(allowed_teams=['team6'])
def feusers(request):
    appusers = LoginAppuser.objects.all().order_by('empcode')
    teams = Team.objects.all()
    template = loader.get_template('userManagement/feusers.html')
    context = {
        'appusers': appusers,
        'teams':teams
    }
    return HttpResponse(template.render(context, request))


@login_required
@allowed_users(allowed_teams=['team6'])
def teams(request):
    teams = Team.objects.all().order_by('id')
    return render(request, 'userManagement/teams.html', {'teams': teams})


@login_required
@allowed_users(allowed_teams=['team6'])
def insertEmployee(request):
    method = False
    if request.method == 'POST':
        method = True
    pan=True
    if method and request.POST.get('pan'):
        pan = False
        pannum = request.POST.get('pan')
        y=pannum[0:5]
        x=pannum[9:10]
        t=pannum[5:9]
        if len(pannum)==10:    
            if pannum.isupper()==True and y.isalpha()==True and x.isalpha()==True and t.isdigit()==True:       
                print("valid pan number")
                pan=True    
    ifsc = True
    if method and request.POST.get('bankifsc'):
        ifsc = False
        ifsccode = request.POST.get('bankifsc')
        response = requests.get(
            "https://ifsc.razorpay.com/"+ifsccode)
        print(response.status_code)
        if response.status_code == 200:
            ifsc = True
        else:
            ifsc = False
    emc=True
    if method and request.POST.get('empcode'):
        if Employee.objects.filter(empcode=request.POST.get('empcode')):
            emc=False
    eml=True
    if method and request.POST.get('empemail'):
        if Employee.objects.filter(empemail=request.POST.get('email')):
            eml=False
    aadhaar=True
    if method and request.POST.get('aadhaar'):
        if Employee.objects.filter(aadhaar=request.POST.get('aadhaar')):
            aadhaar=False
        if aadhaar and len(request.POST.get('aadhaar'))==12:
            aadhaar=True
        elif aadhaar and len(aadhaar=request.POST.get('aadhaar'))!=12:
            aadhaar=False
    acno=True
    if method and request.POST.get('bankacno'):
        acno=False
        if len(str(request.POST.get('bankacno')))>8 and len(str(request.POST.get('bankacno')))<19:
            acno=True
    rf=True
    if method and request.POST.get('rfid'):
        if Employee.objects.filter(rfid=request.POST.get('rfid')):
            rf=False
    act = True
    if method and not request.POST.get('actstatus'):
        act = False
    if method and aadhaar and acno and ifsc and pan and emc and eml and rf and act and request.POST.get('empname') and (request.POST.get('mobile1') or request.POST.get('team') or request.POST.get('site') or request.POST.get('pincode') or request.POST.get('address') or request.POST.get('mobile2') or request.POST.get('bankacno') or request.POST.get('bankachname') or request.POST.get('pan') or request.POST.get('aadhaar') or request.POST.get('gender') or request.POST.get('dob') or request.POST.get('joiningdate') or request.POST.get('eduqual') or request.POST.get('experience') or request.POST.get('maritalstatus') or request.POST.get('depender') or request.POST.get('refname') or request.POST.get('refaddress') or request.POST.get('rfid') or request.POST.get('sifacode') or request.POST.get('accesstype') or request.POST.get('sifaserialnumber') or request.POST.get('empshortcode')):
        saverecord = Employee()
        saverecord.empcode = request.POST.get('empcode')
        saverecord.empname = request.POST.get('empname')
        saverecord.empemail = request.POST.get('empemail')
        if request.POST.get('team'):
            saverecord.team = request.POST.get('team')
        if request.POST.get('site'):
            saverecord.site = request.POST.get('site')
        if request.POST.get('address'):
            saverecord.address = request.POST.get('address')
        if request.POST.get('pincode'):
            saverecord.citycode = request.POST.get('pincode')
        saverecord.mobile1 = request.POST.get('mobile1')
        if request.POST.get('mobile2'):
            saverecord.mobile2 = request.POST.get('mobile2')
        if request.POST.get('bankacno'):
            saverecord.bankacno = request.POST.get('bankacno')
        if request.POST.get('bankifsc'):
            saverecord.bankifsc = request.POST.get('bankifsc')
        if request.POST.get('acholdername'):
            saverecord.acholdername = request.POST.get('acholdername')
        if request.POST.get('pan'):
            saverecord.pan = request.POST.get('pan')
        if request.POST.get('aadhaar'):
            saverecord.aadhaar = request.POST.get('aadhaar')
        if request.POST.get('gender'):
            saverecord.gender = request.POST.get('gender')
        if request.POST.get('dob'):
            saverecord.dob = request.POST.get('dob')
        if request.POST.get('joiningdate'):
            saverecord.joiningdate = request.POST.get('joiningdate')
        if request.POST.get('eduqual'):
            saverecord.eduqual = request.POST.get('eduqual')
        if request.POST.get('experience'):
            saverecord.experience = request.POST.get('experience')
        if request.POST.get('maritalstatus'):
            saverecord.maritalstatus = request.POST.get('maritalstatus')
        if request.POST.get('dependants'):
            saverecord.dependants = request.POST.get('dependants')
        if request.POST.get('refname'):
            saverecord.refname = request.POST.get('refname')
        if request.POST.get('refaddress'):
            saverecord.refaddress = request.POST.get('refaddress')
        if request.POST.get('rfid'):
            saverecord.rfid = request.POST.get('rfid')
        if request.POST.get('sifacode'):
            saverecord.sifacode = request.POST.get('sifacode')
        if request.POST.get('accesstype'):
            saverecord.accesstype = request.POST.get('accesstype')
        if request.POST.get('sifaserialnumber'):
            saverecord.sifaserialnumber = request.POST.get(
                'sifaserialnumber')
        if request.POST.get('empshortcode'):
            saverecord.empshortcode = request.POST.get('empshortcode')
        if request.POST.get('actstatus'):
            saverecord.actstatus = request.POST.get('actstatus')
        saverecord.usercreated = 0
        saverecord.save()
        return redirect('../../employees')
    else:
        if method:
            if not emc:
                messages.warning(request, 'Employee code already exists!')
            if not ifsc:
                messages.warning(request, 'Please enter valid IFSC code!')
            if not pan:
                messages.warning(request, 'Please enter valid PAN Number!')
            if not rf:
                messages.warning(request, 'RFID already exists!')
            if not eml:
                messages.warning(request, 'Email already exists!')
            if not act:
                messages.warning(request, 'Please select activity status!')
            if not aadhaar:
                messages.warning(request, 'Aadhaar No can be of 12 digits! Aadhaar already exists!')
            if not acno:
                messages.warning(request, 'Bank Account No can be of min 9 and max 18 digits')
            saverecord = Employee()
            saverecord.empcode = request.POST.get('empcode')
            saverecord.empname = request.POST.get('empname')
            saverecord.team = request.POST.get('team')
            saverecord.site = request.POST.get('site')
            saverecord.address = request.POST.get('address')
            saverecord.pincode = request.POST.get('pincode')
            saverecord.empemail = request.POST.get('empemail')
            saverecord.mobile1 = request.POST.get('mobile1')
            saverecord.mobile2 = request.POST.get('mobile2')
            saverecord.bankacno = request.POST.get('bankacno')
            saverecord.bankifsc = request.POST.get('bankifsc')
            saverecord.acholdername = request.POST.get('acholdername')
            saverecord.pan = request.POST.get('pan')
            saverecord.aadhaar = request.POST.get('aadhaar')
            saverecord.gender = request.POST.get('gender')
            saverecord.dob = request.POST.get('dob')
            saverecord.joiningdate = request.POST.get('joiningdate')
            saverecord.eduqual = request.POST.get('eduqual')
            saverecord.experience = request.POST.get('experience')
            saverecord.maritalstatus = request.POST.get('maritalstatus')
            saverecord.dependants = request.POST.get('dependants')
            saverecord.refname = request.POST.get('refname')
            saverecord.refaddress = request.POST.get('refaddress')
            saverecord.rfid = request.POST.get('rfid')
            saverecord.sifacode = request.POST.get('sifacode')
            saverecord.accesstype = request.POST.get('accesstype')
            saverecord.sifaserialnumber = request.POST.get('sifaserialnumber')
            saverecord.empshortcode = request.POST.get('empshortcode')
            saverecord.actstatus = request.POST.get('actstatus')
            return render(request, 'userManagement/addEmployee.html', {'saverecord':saverecord})
        teams = Team.objects.all()
        sites = Site.objects.all()
        employees = Employee.objects.all()
        return render(request, 'userManagement/addEmployee.html', {'sites': sites, 'teams': teams,'employees': employees})



def insertTeam(request):
    if request.method == 'POST':
        if request.POST.get('id') and request.POST.get('name'):
            saverecord = Team()
            saverecord.id = request.POST.get('id')
            saverecord.name = request.POST.get('name')
            saverecord.save()
            teams = Team.objects.all()
            return render(request, 'userManagement/teams.html', {'teams': teams})
    else:
        return render(request, 'userManagement/addTeam.html', {})

@login_required
@allowed_users(allowed_teams=['team6'])
def viewUser(request, user_id):
    getuser = LoginAppuser.objects.get(user_id=user_id)
    teams = Team.objects.all()
    return render(request, 'userManagement/viewUser.html', {'getuser': getuser,'teams': teams})

@login_required
@allowed_users(allowed_teams=['team6'])
def viewEmployee(request, empid):
    getempid = Employee.objects.get(empid=empid)
    return render(request, 'userManagement/viewEmployee.html', {'getempid': getempid})


@login_required
@allowed_users(allowed_teams=['team6'])
def editUser(request, user_id):
    method=False
    if request.method=='POST':
        method=True
    team=False
    if method and (request.POST.get('team1') == 'Yes' or request.POST.get('team2') == 'Yes' or request.POST.get('team3') == 'Yes' or request.POST.get('team4') == 'Yes' or request.POST.get('team5') == 'Yes' or request.POST.get('team6') == 'Yes' or request.POST.get('team7') == 'Yes' or request.POST.get('team8') == 'Yes' or request.POST.get('team9') == 'Yes' or request.POST.get('team10') == 'Yes' or request.POST.get('team11') == 'Yes' or request.POST.get('team12') == 'Yes' or request.POST.get('team13') == 'Yes' or request.POST.get('team14') == 'Yes' or request.POST.get('team15') == 'Yes'):
        team=True
    act = True
    if method and not request.POST.get('act_status'):
        act = False
    if method and team and act:
        if request.POST.get('team1'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team1=request.POST.get('team1'))
        if request.POST.get('team2'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team2=request.POST.get('team2'))
        if request.POST.get('team3'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team3=request.POST.get('team3'))
        if request.POST.get('team4'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team4=request.POST.get('team4'))
        if request.POST.get('team5'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team5=request.POST.get('team5'))
        if request.POST.get('team6'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team6=request.POST.get('team6'))
        if request.POST.get('team7'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team7=request.POST.get('team7'))
        if request.POST.get('team8'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team8=request.POST.get('team8'))
        if request.POST.get('team9'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team9=request.POST.get('team9'))
        if request.POST.get('team10'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team10=request.POST.get('team10'))
        if request.POST.get('team11'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team11=request.POST.get('team11'))
        if request.POST.get('team12'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team12=request.POST.get('team12'))
        if request.POST.get('team13'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team13=request.POST.get('team13'))
        if request.POST.get('team14'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team14=request.POST.get('team14'))
        if request.POST.get('team15'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                team15=request.POST.get('team15'))
        if request.POST.get('act_status'):
            LoginAppuser.objects.all().filter(user_id=user_id).update(
                act_status=request.POST.get('act_status'))
        return redirect('../../feusers')
    else:
        if method:
            if not team:
                messages.warning(request, 'Please choose atleast one team!')
            if not act:
                messages.warning(request, 'Please select activity status!')
        getuser = LoginAppuser.objects.get(user_id=user_id)
        teams = Team.objects.all()
        return render(request, 'userManagement/editUser.html', {'getuser': getuser,'teams':teams})


@login_required
@allowed_users(allowed_teams=['team6'])
def editEmployee(request, empid):
    getempid = Employee.objects.get(empid=empid)
    teams = Team.objects.all()
    sites = Site.objects.all()
    context = {
        'getempid': getempid,
        'teams': teams,
        'sites': sites,
    }
    method = False
    if request.method == 'POST':
        method = True
    pan=True
    if method and request.POST.get('pan'):
        if not getempid.pan==request.POST.get('pan'):
            pan = False
            pannum = request.POST.get('pan')
            y=pannum[0:5]
            x=pannum[9:10]
            t=pannum[5:9]
            if len(pannum)==10:    
                if pannum.isupper()==True and y.isalpha()==True and x.isalpha()==True and t.isdigit()==True:
                    pan=True    
    ifsc = True
    if method and request.POST.get('bankifsc'):
        if not getempid.bankifsc==request.POST.get('bankifsc'):
            ifsc = False
            ifsccode = request.POST.get('bankifsc')
            response = requests.get(
                "https://ifsc.razorpay.com/"+ifsccode)
            if response.status_code == 200:
                ifsc = True
            else:
                ifsc = False
    emc=True
    if method and request.POST.get('empcode'):
        if not getempid.empcode==request.POST.get('empcode'):
            if Employee.objects.filter(empcode=request.POST.get('empcode')):
                emc=False
    aadhaar=True
    if method and request.POST.get('aadhaar'):
        if not getempid.aadhaar==request.POST.get('aadhaar'):
            aadhaar=False
            if not Employee.objects.filter(aadhaar=request.POST.get('aadhaar')):
                aadh=request.POST.get('aadhaar')
                if len(aadh)==12:
                    aadhaar=True
    acno=True
    if method and request.POST.get('bankacno'):
        if not getempid.bankacno==request.POST.get('bankacno'):
            acno=False
            if len(str(request.POST.get('bankacno')))>8 and len(str(request.POST.get('bankacno')))<19:
                acno=True
    eml=True
    if method and request.POST.get('email'):
        if not getempid.empemail==request.POST.get('email'):
            if Employee.objects.filter(empemail=request.POST.get('email')):
                eml=False
    rf=True
    if method and request.POST.get('rfid'):
        if not getempid.rfid==request.POST.get('rfid'):
            if Employee.objects.filter(rfid=request.POST.get('rfid')):
                rf=False
    act = True
    if method and not request.POST.get('actstatus'):
        act = False
    if method and aadhaar and acno and pan and ifsc and emc and eml and rf and act:
        if request.POST.get('empcode'):
            Employee.objects.all().filter(empid=empid).update(
                empcode=request.POST.get('empcode'))
        if request.POST.get('empname'):
            Employee.objects.all().filter(empid=empid).update(
                empname=request.POST.get('empname'))
        if request.POST.get('team'):
            Employee.objects.all().filter(empid=empid).update(team=request.POST.get('team'))
        if request.POST.get('site'):
            Employee.objects.all().filter(empid=empid).update(site=request.POST.get('site'))
        if request.POST.get('address'):
            Employee.objects.all().filter(empid=empid).update(
                address=request.POST.get('address'))
        if request.POST.get('empemail'):
            Employee.objects.all().filter(empid=empid).update(
                empemail=request.POST.get('empemail'))
        if request.POST.get('pincode'):
            Employee.objects.all().filter(empid=empid).update(
                pincode=request.POST.get('pincode'))
        if request.POST.get('mobile1'):
            Employee.objects.all().filter(empid=empid).update(
                mobile1=request.POST.get('mobile1'))
        if request.POST.get('mobile2'):
            Employee.objects.all().filter(empid=empid).update(
                mobile2=request.POST.get('mobile2'))
        if request.POST.get('bankacno'):
            Employee.objects.all().filter(empid=empid).update(
                bankacno=request.POST.get('bankacno'))
        if request.POST.get('bankifsc'):
            Employee.objects.all().filter(empid=empid).update(
                bankifsc=request.POST.get('bankifsc'))
        if request.POST.get('bankachname'):
            Employee.objects.all().filter(empid=empid).update(
                acholdername=request.POST.get('bankachname'))
        if request.POST.get('pan'):
            Employee.objects.all().filter(empid=empid).update(pan=request.POST.get('pan'))
        if request.POST.get('aadhaar'):
            Employee.objects.all().filter(empid=empid).update(
                aadhaar=request.POST.get('aadhaar'))
        if request.POST.get('gender'):
            Employee.objects.all().filter(empid=empid).update(
                gender=request.POST.get('gender'))
        if request.POST.get('dob'):
            Employee.objects.all().filter(empid=empid).update(dob=request.POST.get('dob'))
        if request.POST.get('joiningdate'):
            Employee.objects.all().filter(empid=empid).update(
                joiningdate=request.POST.get('joiningdate'))
        if request.POST.get('eduqual1'):
            Employee.objects.all().filter(empid=empid).update(
                eduqual=request.POST.get('eduqual1'))
        if request.POST.get('eduqual2'):
            Employee.objects.all().filter(empid=empid).update(
                eduqual=request.POST.get('eduqual2'))
        if request.POST.get('experience'):
            Employee.objects.all().filter(empid=empid).update(
                experience=request.POST.get('experience'))
        if request.POST.get('maritalstatus'):
            Employee.objects.all().filter(empid=empid).update(
                maritalstatus=request.POST.get('maritalstatus'))
        if request.POST.get('dependants'):
            Employee.objects.all().filter(empid=empid).update(
                dependants=request.POST.get('dependants'))
        if request.POST.get('refname'):
            Employee.objects.all().filter(empid=empid).update(
                refname=request.POST.get('refname'))
        if request.POST.get('refaddress'):
            Employee.objects.all().filter(empid=empid).update(
                refaddress=request.POST.get('refaddress'))
        if request.POST.get('rfid'):
            Employee.objects.all().filter(empid=empid).update(rfid=request.POST.get('rfid'))
        if request.POST.get('sifacode'):
            Employee.objects.all().filter(empid=empid).update(
                sifacode=request.POST.get('sifacode'))
        if request.POST.get('accesstype'):
            Employee.objects.all().filter(empid=empid).update(
                accesstype=request.POST.get('accesstype'))
        if request.POST.get('sifaserialnumber'):
            Employee.objects.all().filter(empid=empid).update(
                sifaserialnumber=request.POST.get('sifaserialnumber'))
        if request.POST.get('empshortcode'):
            Employee.objects.all().filter(empid=empid).update(
                empshortcode=request.POST.get('empshortcode'))
        if request.POST.get('actstatus'):
            Employee.objects.all().filter(empid=empid).update(
                actstatus=request.POST.get('actstatus'))
        return redirect('../../employees')
    else:
        if method:
            if not emc:
                messages.warning(request, 'Employee code already exists!')
            if not ifsc:
                messages.warning(request, 'Please enter valid IFSC code!')
            if not pan:
                messages.warning(request, 'Please enter valid PAN Number!')
            if not rf:
                messages.warning(request, 'RFID already exists!')
            if not eml:
                messages.warning(request, 'Email already exists!')
            if not act:
                messages.warning(request, 'Please select activity status!')
            if not aadhaar:
                messages.warning(request, 'Aadhaar No can be of 12 digits! Aadhaar already exists!')
            if not acno:
                messages.warning(request, 'Bank Account No can be of min 9 and max 18 digits')
            return render(request, 'userManagement/editEmployee.html', context)
    return render(request, 'userManagement/editEmployee.html', context)

@login_required
@allowed_users(allowed_teams=['team6'])
def editTeam(request,id):
    getteam = Team.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('name'):
            Team.objects.all().filter(id=id).update(name=request.POST.get('name'))
            return redirect('../../teams')
    return render(request, 'userManagement/editTeam.html', {'getteam': getteam})


@login_required
@allowed_users(allowed_teams=['team6'])
def deleteEmployee(request, empid):
    getempid = Employee.objects.get(empid=empid)
    Employee.objects.all().filter(empid=empid).update(actstatus="Inactive")
    return redirect('../../employees')
    
@login_required
@allowed_users(allowed_teams=['team6'])
def deleteUser(request, user_id):
    getuser = LoginAppuser.objects.get(user_id=user_id)
    LoginAppuser.objects.all().filter(user_id=user_id).update(
                act_status="Inactive")
    return redirect('../../feusers')