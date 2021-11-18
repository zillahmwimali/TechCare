from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL



    
class Households(models.Model):
    contact_person_first_name = models.CharField(max_length=15)
    contact_persons_last_name = models.CharField(max_length=20)
    ID_number = models.CharField(max_length=8)
    household_area = models.CharField( max_length = 30)
    number_of_household_members = models.IntegerField()
    contact_persons_income = models.BigIntegerField()


    def __str__(self):
        return self.contact_person_first_name


class GeneralAssessment(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    house = models.ForeignKey(Households,on_delete=CASCADE,null=True)
    area = models.CharField(max_length=12)
    number_of_pregnant_women = models.PositiveSmallIntegerField()
    number_of_newborns = models.PositiveSmallIntegerField()
    number_of_children_under_5_years_of_age = models.PositiveSmallIntegerField()
    number_of_vaccinated_children = models.PositiveSmallIntegerField()
    number_of_people_living_with_diabilities = models.PositiveSmallIntegerField()
    number_of_elderly = models.PositiveSmallIntegerField()
    number_of_orphans = models.PositiveSmallIntegerField()
    number_of_persons_living_with_chronic_diseases = models.PositiveSmallIntegerField()
    do_you_have_any_sick_person_in_this_household = models.BooleanField(choices=BOOL_CHOICES)
    do_you_have_health_insurance = models.BooleanField( choices=BOOL_CHOICES)
    remarks = models.TextField()

    def __str__(self):
        return self.house.contact_person_first_name


class MotherAssessment(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    house = models.ForeignKey(Households,on_delete=CASCADE,null=True)
    area = models.CharField(max_length=12)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    have_you_lost_an_infant_before = models.BooleanField(choices=BOOL_CHOICES)
    how_many= models.PositiveSmallIntegerField()
    how_far_long_is_your_pregnancy = models.PositiveSmallIntegerField()
    what_is_your_expected_day_of_delivery = models.DateField()
    do_you_have_any_complications = models.BooleanField(choices=BOOL_CHOICES)
    describe_the_complication = models.CharField(max_length=50)
    do_you_go_to_clinic = models.BooleanField(choices=BOOL_CHOICES)
    which_clinic = models.CharField(max_length=20)
    when_was_the_last_time_you_visited_a_clinic = models.DateField()
    do_take_any_supplements = models.BooleanField(choices=BOOL_CHOICES)
    if_yes_which_one= models.PositiveSmallIntegerField()
    do_you_have_Linda_Mama = models.BooleanField(choices=BOOL_CHOICES)
    remarks = models.TextField()

    def __str__(self):
        return self.first_name


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
       ("Family planning","Family planning"),
       ("Other","Other")
   )
    condition =models.CharField(
       max_length = 30,
       choices = condition_choice,
   )
    have_you_visited_any_hospital_before = models.BooleanField()
    which_one = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)
    brief_description_of_the_condition = models.TextField()


    def __str__(self):
        return self.patients_first_name

class ChildAssessment(models.Model):
    house = models.ForeignKey(Households,on_delete=CASCADE,null=True)
    childs_first_name = models.CharField(max_length=15)
    childs_last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    has_she_or_she_been_vaccinated = models.BooleanField(null=True)


    def __str__(self):
        return self.childs_first_name


class Mother_referral(models.Model):
    referree = models.ForeignKey(Households,on_delete=CASCADE)
    mothers_first_name = models.CharField(max_length=15)
    mothers_last_name = models.CharField(max_length=20)
    home_area = models.CharField(max_length=20)
    hospital_name = models.CharField(max_length=20)
    condition_choice = (
       ("Cough","Cough"),
       ("Diarrhoea","Diarrhoea"),
       ("Epilepsy","Epilepsy"),
       ("Pregnancy","Pregnancy"),
       ("Nutrition","Nutrition"),
       ("Family planning","Family planning"),
       ("Other","Other")
   )
    condition =models.CharField(
       max_length = 30,
       choices = condition_choice,
   )
    date = models.DateTimeField(null=True)


    def __str__(self):
        return self.mothers_first_name




