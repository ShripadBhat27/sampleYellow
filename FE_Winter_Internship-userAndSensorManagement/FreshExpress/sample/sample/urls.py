"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
import django
from django import urls
from django.contrib import admin
from django.urls import path, include
from userManagement import views as uv
from Login import views as lv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', uv.employees, name='employees'),
    path('addEmployee/', uv.insertEmployee, name='add_employee'),
    path('feusers/', uv.feusers, name='feusers'),
    path('teams/', uv.teams, name='teams'),
    path('viewUser/<int:user_id>', uv.viewUser, name='view_user'),
    path('editUser/<int:user_id>', uv.editUser, name='edit_user'),
    path('deleteUser/<int:user_id>', uv.deleteUser, name='delete_user'),
    path('deleteEmployee/<int:empid>', uv.deleteEmployee, name='delete_employee'),
    path('editEmployee/<int:empid>', uv.editEmployee, name='edit_employee'),
    path('editTeam/<int:id>', uv.editTeam, name='edit_team'),
    path('viewEmployee/<int:empid>', uv.viewEmployee, name='view_employee'),
    path('dashboard/', lv.dashboard, name='dashboard'),
    path('newpass/', lv.newpassword, name='newpass'),
    path('resetpass/', lv.resetpassword, name='resetpass'),
    path('', lv.customregister, name='landing'),
    path('accounts/login/', lv.customlogin, name="login"),
    path('accounts/logout/', lv.customlogout, name="logout"),
    path('userProfile/<int:id>', lv.userProfile, name='userprof'),
]
