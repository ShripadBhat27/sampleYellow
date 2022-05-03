from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# class AuthUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


class LoginAppuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Field name made lowercase.
    empcode = models.CharField(
        db_column='empCode', unique=True, max_length=8, blank=True, null=True)
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
    act_status = models.CharField(max_length=10, blank=True, null=True)
    chat_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Login_appuser'

    def __str__(self):
        id = self.user_id
        user = User.objects.get(id=id)
        return user.username


@receiver(post_save, sender=User)
def create_appuser(sender, instance, created, **kwargs):
    if created:
        appuser = LoginAppuser.objects.create(user_id=instance.id)
        appuser.save()


class Role(models.Model):
    role_rolecode = models.CharField(primary_key=True, max_length=50)
    role_rolename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'role'


class SystemUsers(models.Model):
    u_userid = models.AutoField(primary_key=True)
    u_username = models.CharField(max_length=100)
    u_password = models.CharField(max_length=255)
    u_rolecode = models.ForeignKey(Role, models.DO_NOTHING, db_column='u_rolecode')

    class Meta:
        managed = False
        db_table = 'system_users'


@receiver(post_save, sender=User)
def create_sysuser(sender, instance, created, **kwargs):
    if created:
        sysuser = SystemUsers.objects.create(u_username=instance.username,u_rolecode=Role.objects.get(role_rolecode="USER"))
        sysuser.save()

# @receiver(post_save, sender=User)
# def save_appuser(sender, instance, **kwargs):
#     instance.appuser.save()


# @receiver(post_save, sender=User)
# def create_appuser(sender, instance, created, **kwargs):
#     if created:
#         AppUser.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_appuser(sender, instance, **kwargs):
#     instance.appuser.save()
