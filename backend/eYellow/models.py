from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=20,null=True)
    mobileno = models.IntegerField(db_column='mobileNo', unique=True,null=True)  # Field name made lowercase.
    address = models.CharField(max_length=45,null=True)

    class Meta:
        managed = False
        db_table = 'customer'

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.create(user_id=instance.id)
        customer.save()