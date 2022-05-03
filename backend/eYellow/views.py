from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CustomerSerializer
from .models import Customer

# Create your views here.

def customregister(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = False
    if method and not User.objects.filter(username=request.POST.get('username')):
        unm = True
    eml=False
    if method and not User.objects.filter(email=request.POST.get('username')):
        eml=True
    if method and unm and eml:
        saverecord = User()
        saverecord.username = request.POST.get('username')
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        saverecord.set_password(password)
        send_mail('Registration Successful', 'Congratulations '+saverecord.username+', you have been registered successfully! Welcome to Yellow Pages! Your credentials are - Username: '+saverecord.username+'; Password: '+password+' , Regards, Yellow Pages Team', 'chinmaykulkarnica2018@gmail.com', request.POST.get('email'), fail_silently=False)
        saverecord.save()
        messages.warning(request, 'Please check your registered email for login credentials.')
        user = User.objects.get(username=request.POST.get('username'))
        # Customer.objects.filter(user_id=user.id).update(empcode=request.POST.get('empcode'))
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
                messages.warning(request, 'Passwords don\'t match!')
            saverecord = request.POST.get('username')
        return render(request, 'registration/customregister.html', {'saverecord': saverecord, 'empcode': empcode, 'employees': employees})


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


