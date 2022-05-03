import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import LoginAppuser,SystemUsers
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.mail import send_mail
from sample.settings import MESSAGE_STORAGE
from userManagement.models import Employee
from django.contrib.auth import authenticate, login, logout
import random
import string

# Create your views here.

# @login_required
# @transaction.atomic
# def update_appuser(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         appuser_form = AppUserForm(request.POST, instance=request.user.appuser)
#         if user_form.is_valid() and appuser_form.is_valid():
#             user_form.save()
#             appuser_form.save()
#             messages.success(request,'Your profile was successfully updated!')
#             return redirect('settings:appuser')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_form = UserForm(instance=request.user)
#         appuser_form = AppUserForm(instance=request.user.appuser)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'appuser_form': appuser_form
#     })


# def add_appuser(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         appuser_form = AppUserForm(request.POST)
#         if user_form.is_valid() and appuser_form.is_valid():
#             user=user_form.save()
#             appuser=appuser_form.save(commit=False)
#             if appuser.user_id is None:
#                 appuser.user_id = user.id
#             appuser_form.save()
#             messages.success(request,'Your user was successfully added!')
#             return render(request,'Login/login.html',{})
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_form = UserForm()
#         appuser_form = AppUserForm()
#     return render(request, 'CustomUsers/customregister.html', {
#         'user_form': user_form,
#         'appuser_form': appuser_form
#     })

def customregister(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = False
    if method and not User.objects.filter(username=request.POST.get('username')):
        unm = True
    emc = False
    if method and not LoginAppuser.objects.filter(empcode=request.POST.get('empcode')):
        emc = True
    eml = False
    if method:
        emp = Employee.objects.get(empcode=request.POST.get('empcode'))
        if emp.empemail:
            eml = True
    if method and unm and emc and eml:
        saverecord = User()
        saverecord.username = request.POST.get('username')
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        emp = Employee.objects.get(empcode=request.POST.get('empcode'))
        print(password)
        saverecord.set_password(password)
        send_mail('FE User Created', 'Congratulations '+saverecord.username+', you have been registered successfully! Welcome to Fresh Express Users! Your credentials are - Username: '+saverecord.username+'; Password: '+password+' , Regards, Fresh Express', 'chinmaykulkarnica2018@gmail.com', [emp.empemail], fail_silently=False)
        saverecord.save()
        messages.warning(request, 'Please check your registered email for login credentials.')
        user = User.objects.get(username=request.POST.get('username'))
        LoginAppuser.objects.filter(user_id=user.id).update(empcode=request.POST.get('empcode'))
        print('success')
        return render(request, 'registration/login.html', {})
    else:
        saverecord = ''
        empcode = 0
        if request.POST.get('empcode'):
            empcode = request.POST.get('empcode')
        if method:
            if not unm:
                messages.warning(request, 'Username already exists!')
            if request.POST.get('password1') != request.POST.get('password2'):
                messages.warning(request, 'Passwords don\'nt match!')
            if not emc:
                messages.warning(request, 'Employee Code already exists!')
            if emc and not eml:
                messages.warning(
                    request, 'Employee Email not registered. Please register Email for Employee Code='+empcode+' and try again!')
            saverecord = request.POST.get('username')
        employees = Employee.objects.filter(usercreated=0).values('empcode')
        return render(request, 'registration/customregister.html', {'saverecord': saverecord, 'empcode': empcode, 'employees': employees})


def customlogin(request):
    method = False
    if request.method == 'POST':
        method = True
        unm = True
        if not User.objects.filter(username=request.POST.get('username')):
            unm = False
        para = False
    if method and unm:
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            para=True
    if method and unm and para:
        login(request, user)
        appuser = LoginAppuser.objects.get(user_id=request.user.id)
        emp = Employee.objects.get(empcode=appuser.empcode)
        if emp.usercreated:
            return redirect('../../dashboard')
        else:
            Employee.objects.filter(empcode=appuser.empcode).update(usercreated=1)
            return render(request, 'registration/newpass.html', {})
    else:
        if method:
            if not unm:
                messages.warning(request, 'Username doesn\'t exist!')
            if not para:
                messages.warning(request, 'Please enter valid password!')
            if request.POST.get('username'):
                object = request.POST.get('username')
            return render(request, 'registration/login.html', {'object': object})
        return render(request, 'registration/login.html', {})


@login_required
def newpassword(request):
    method = False
    if request.method == 'POST':
        method = True
    para = False
    while method and request.POST.get('password1') == request.POST.get('password2'):
        password = request.POST.get('password1')
        if len(password) < 6 and len(password) > 11:
            para = False
            break
        elif not re.search("[A-Z]", password):
            para = False
            break
        elif not re.search("[0-9]", password):
            para = False
            break
        elif not re.search("[_@$]", password):
            para = False
            break
        elif re.search("\s", password):
            para = False
            break
        else:
            para = True
            break
    if method and para:
        saverecord = User.objects.get(username=request.user)
        saverecord.set_password(request.POST.get('password1'))
        str = saverecord.password
        User.objects.filter(username=request.user.username).update(password=str)
        appuser = LoginAppuser.objects.get(user_id=request.user.id)
        emp = Employee.objects.get(empcode=appuser.empcode)
        print(emp)
        send_mail('FE User Password Updated', 'Dear '+saverecord.username+', your password have been updated successfully! Regards, Fresh Express','chinmaykulkarnica2018@gmail.com', [emp.empemail], fail_silently=False)
        print('success')
        logout(request)
        return render(request, 'registration/login.html', {})
    else:
        if method:
            if request.POST.get('password1') != request.POST.get('password2'):
                messages.warning(request, 'Passwords don\'nt match!')
            if not para:
                messages.warning(
                    request, 'Password must contain min 6 and max 11 characters,at least one alphabet should be Lower Case [a-z], at least one alphabet should be of Upper Case [A-Z], at least 1 number or digit between [0-9], at least 1 character from [ _ or @ or $ ], blank spaces are restricted.')
        return render(request, 'registration/newpass.html', {})


@login_required
def dashboard(request):
    return render(request, 'registration/welcome.html', {})


def resetpassword(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = False
    emc = False
    status=False
    if method:
        if User.objects.filter(username=request.POST.get('username')):
            usr=User.objects.get(username=request.POST.get('username'))
            unm = True
        if LoginAppuser.objects.filter(empcode=request.POST.get('empcode')):
            logusr=LoginAppuser.objects.get(empcode=request.POST.get('empcode'))
            emc = True
        if unm and emc:
            if logusr.user_id==usr.id:
                status=True
    eml = False
    if method:
        emp = Employee.objects.get(empcode=request.POST.get('empcode'))
        if emp.empemail:
            eml = True
    if method and unm and emc and eml and status:
        saverecord = User()
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        emp = Employee.objects.get(empcode=request.POST.get('empcode'))
        print(password)
        saverecord.set_password(password)
        str = saverecord.password
        User.objects.filter(username=request.POST.get('username')).update(password=str)
        send_mail('FE User Created', 'Congratulations '+saverecord.username+', you have been registered successfully! Welcome to Fresh Express Users! Your credentials are - Username: '+saverecord.username+' ; Password: '+password+' , Regards, Fresh Express', 'chinmaykulkarnica2018@gmail.com', [emp.empemail], fail_silently=False)
        user = User.objects.get(username=request.POST.get('username'))
        Employee.objects.filter(empcode=request.POST.get('empcode')).update(usercreated=0)
        messages.warning(request, 'Please check your registered email for login credentials.')
        print('success')
        return render(request, 'registration/login.html', {})
    else:
        saverecord = ''
        empcode = 0
        if request.POST.get('empcode'):
            empcode = request.POST.get('empcode')
        if method:
            if not unm:
                messages.warning(request, 'Username doesn\'nt exists!')
            if not emc:
                messages.warning(request, 'Employee Code doesn\'nt exists!')
            if emc and not eml:
                messages.warning(request, 'Employee Email not registered. Please register Email for Employee Code='+empcode+' and try again!')
            if not status:
                messages.warning(request, 'Check details again. User with provided details doesn\'nt exists!')
            saverecord = request.POST.get('username')
        employees = Employee.objects.filter(usercreated=1).values('empcode')
        return render(request, 'registration/resetpass.html', {'saverecord': saverecord, 'empcode': empcode, 'employees': employees})


@login_required
def userProfile(request,id):
    method=False
    if request.method=='POST':
        method=True
    unm=True
    if method and request.user.username!=request.POST.get('username'):
        unm=False
        if not User.objects.filter(username=request.POST.get('username')):
            unm=True
    # if method and User.objects.filter(username=request.POST.get('username')):
    #     unm=False
    #     user=User.objects.get(username=request.POST.get('username'))
    #     if user.id==request.user.id:
    #         unm=True
    para = False
    while method and request.POST.get('password'):
        password = request.POST.get('password')
        if len(password) < 6 and len(password) > 11:
            para = False
            break
        elif not re.search("[A-Z]", password):
            para = False
            break
        elif not re.search("[0-9]", password):
            para = False
            break
        elif not re.search("[_@$]", password):
            para = False
            break
        elif re.search("\s", password):
            para = False
            break
        else:
            para = True
            break
    if unm and para:
        saverecord=User.objects.get(username=request.user.username)
        User.objects.filter(username=request.user.username).update(username=request.POST.get('username'))
        SystemUsers.objects.filter(username=request.user.username).update(username=request.POST.get('username'))
        saverecord.set_password(password)
        str = saverecord.password
        User.objects.filter(username=request.user.username).update(password=str)
        appuser = LoginAppuser.objects.get(user_id=request.user.id)
        emp = Employee.objects.get(empcode=appuser.empcode)
        print(emp)
        send_mail('FE User Password Updated', 'Dear '+saverecord.username+', your password have been updated successfully! Regards, Fresh Express','chinmaykulkarnica2018@gmail.com', [emp.empemail], fail_silently=False)
        print('success')
        return redirect('../dashboard/')
    else:
        if method:
            if not unm:
                messages.warning(request, 'Username already exists!')
            if not para:
                messages.warning(request, 'Password must contain min 6 and max 11 characters,at least one alphabet should be Lower Case [a-z], at least one alphabet should be of Upper Case [A-Z], at least 1 number or digit between [0-9], at least 1 character from [ _ or @ or $ ], blank spaces are restricted.')
            username=request.POST.get('username')
            return render(request,'registration/userprofile.html', {'username': username,})
        return render(request,'registration/userprofile.html', {})

        


def customlogout(request):
    logout(request)
    return redirect('login')


# def login_view(request):
#     form = LoginForm(data=request.POST)
#     if form.is_valid():
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse(LOGIN_REDIRECT_URL))
