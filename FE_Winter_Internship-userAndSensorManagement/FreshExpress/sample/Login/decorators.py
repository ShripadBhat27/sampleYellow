from django.http import HttpResponse
from django.shortcuts import redirect
from .models import LoginAppuser
from django.contrib.auth.models import User


def allowed_users(allowed_teams=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            allowance = False
            user = User.objects.get(username=request.user.username)
            appuser = LoginAppuser.objects.get(user_id=user.id)
            for i in allowed_teams:
                if i == "team1":
                    if appuser.team1 == "Yes":
                        allowance = True
                        break
                if i == "team2":
                    if appuser.team2 == "Yes":
                        allowance = True
                        break
                if i == "team3":
                    if appuser.team3 == "Yes":
                        allowance = True
                        break
                if i == "team4":
                    if appuser.team4 == "Yes":
                        allowance = True
                        break
                if i == "team5":
                    if appuser.team5 == "Yes":
                        allowance = True
                        break
                if i == "team6":
                    if appuser.team6 == "Yes":
                        allowance = True
                        break
                if i == "team7":
                    if appuser.team7 == "Yes":
                        allowance = True
                        break
                if i == "team8":
                    if appuser.team8 == "Yes":
                        allowance = True
                        break
                if i == "team9":
                    if appuser.team9 == "Yes":
                        allowance = True
                        break
                if i == "team10":
                    if appuser.team10 == "Yes":
                        allowance = True
                        break
                if i == "team11":
                    if appuser.team11 == "Yes":
                        allowance = True
                        break
                if i == "team12":
                    if appuser.team12 == "Yes":
                        allowance = True
                        break
                if i == "team13":
                    if appuser.team13 == "Yes":
                        allowance = True
                        break
                if i == "team14":
                    if appuser.team14 == "Yes":
                        allowance = True
                        break
                if i == "team15":
                    if appuser.team15 == "Yes":
                        allowance = True
                        break
            if allowance and appuser.act_status=="Active":
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorised to view this page!")
        return wrapper_func
    return decorator
