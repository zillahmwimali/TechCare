
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

Referral=(
    ("G","Google"),
    ("F","Facebook"),
    ("T","Twitter"),
    ("I","Instagram"),
    ("F","Friend"),
)
class Contact(models.Model):
    full_name = models.CharField(max_length=50) 
    phone_number = PhoneNumberField()  
    email =models.EmailField()
    region =models.CharField(max_length=50)
    how_did_you_hear_about_us=models.CharField(max_length=50,choices=Referral,default="Google")
    message=models.TextField(max_length=250)


# Create your models here.
