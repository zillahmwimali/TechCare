from django.conf.urls import url
from django.urls import path
from .views import chwHouseholds,addHousehold,edit_household

urlpatterns = [
    path('household/',chwHouseholds,name='household'),
    path('addHousehold/' , addHousehold, name = 'addHousehold'),
    path('edit_household/' , edit_household, name = 'edit_household')

]

