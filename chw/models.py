from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
import datetime

class Chw(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    phone_number = PhoneNumberField()
    ID_number = models.CharField(max_length=8)
    date_of_birth = models.DateField()
    gender_choice = (
       ("Female","Female"),
       ("Male","Male"),
       ("Other","Other")
   )
    gender = models.CharField(
       max_length = 10,
       choices = gender_choice,
   )
    email = models.EmailField(default='janedoe@gmail.com')
    region_or_location = models.CharField(max_length=30)
    def __str__(self):
       return self.first_name


class Households(models.Model):
    contact_person_first_name = models.CharField(max_length=15)
    contact_persons_last_name = models.CharField(max_length=20)
    phone_number = PhoneNumberField()
    ID_number = models.CharField(max_length=8)
    household_area = models.CharField( max_length = 30)
    number_of_household_members = models.IntegerField()
    contact_persons_income = models.BigIntegerField()
    number_of_pregnant_women = models.PositiveSmallIntegerField()
    number_of_newborns = models.PositiveSmallIntegerField()
    number_of_children_under_5_years_of_age = models.PositiveSmallIntegerField()
    number_of_people_living_with_diabilities = models.PositiveSmallIntegerField()
    number_of_elderly = models.PositiveSmallIntegerField()
    number_of_orphans = models.PositiveSmallIntegerField()
    number_of_persons_living_with_chronic_diseases = models.PositiveSmallIntegerField()
    remarks = models.TextField()

    def __str__(self):
        return self.contact_person_first_name

class Referral(models.Model):
    referree = models.ForeignKey(Households,on_delete=CASCADE)
    patients_first_name = models.CharField(max_length=15)
    patients_last_name = models.CharField(max_length=20)
    home_area = models.CharField(max_length=20)
    hospital_name = models.CharField(max_length=20)
    condition_choice = (
       ("Cough","Cough"),
       ("Diarrhoea","Diarrhoea"),
       ("Epilepsy","Epilepsy"),
       ("Pregnancy","Pregnancy"),
       ("Nutrition","Nutrition"),
       ("Family planning","Family planning")

   )
    condition =models.CharField(
       max_length = 30,
       choices = condition_choice,
   )
    date = models.DateTimeField(null=True)

    brief_description_of_the_condition = models.TextField()

#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



