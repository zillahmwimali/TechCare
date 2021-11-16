from django.db import models

class OrgProfile(models.Model):
    organisation_name=models.CharField(max_length=20)
    membership_number=models.CharField(max_length=10)
    # email=models.EmailField()
    # phone_number=PhoneNumberField()
    email=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=10)
    number_of_community_health_workers=models.PositiveSmallIntegerField()

    def __str__(self):
        return self.organisation_name
# Create your models here.
