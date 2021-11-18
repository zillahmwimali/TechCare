from django.db import models
from .manager import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE, SET_NULL

class User(AbstractUser):
    username = models.CharField(('username'), unique=False,max_length=50)
    email = models.EmailField(('email address'), unique=True)
    is_previously_logged_in=models.BooleanField(default=False)
    is_superadmin = models.BooleanField(('is_superadmin'), default=False)
    is_active = models.BooleanField(('is_active'), default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    ORGANIZATION=1
    CHW=2
    ROLE_CHOICES = (
        (ORGANIZATION, 'ORGANIZATION'),
        (CHW, 'CHW'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True,null=True)
    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        permissions = (
            ('is_organization', 'Can view dashboard'),
            ('is_chw', 'Can view chw app'),
        )
    def __str__(self):
        """stirng representation"""
        return self.email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Chw(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    gender = models.CharField( max_length = 10)
    
    def __str__(self):
        return self.user.first_name
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role==2:
            Chw.objects.create(user=instance)
    else:
        pass


class OrgProfile(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    organisation_name=models.CharField(max_length=20)
    membership_number=models.CharField(max_length=10)
    number_of_community_health_workers=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.organisation_name

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role==2:
            OrgProfile.objects.create(user=instance)
    else:
        pass