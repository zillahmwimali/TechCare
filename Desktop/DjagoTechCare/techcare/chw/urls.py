from django.conf.urls import url
from django.urls import path
from .views import child_assess, chwHouseholds,addHousehold,edit_household,assessments, general_assessment, new_household,referrals,followUp,new_household,child_assess,mother_assess

urlpatterns = [
    path('household/',chwHouseholds,name='household'),
    path('addHousehold/' , addHousehold, name = 'addHousehold'),
    path('edit_household/' , edit_household, name = 'edit_household'),
    path('Referrals/',referrals,name='Referrals'),
    path('follow-up/',followUp,name='followUp'),
    path('new_household/',new_household,name='new_household'),
    path('general_assessment/',general_assessment,name='general_assessment'),
    path('child_assess/',child_assess,name='child_assess'),
    path('mother_assess/',mother_assess,name='mother_assess'),
    path('patient_assessments/',assessments,name='patient_assessments'),

]

