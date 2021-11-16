from django.conf.urls import url
from django.urls import path
from .views import child_assess, chwHouseholds,addHousehold,edit_household,assessments, general_assessment, new_household,referrals,followUp,refer,follow_up,delete_referree,edit_referral,new_household,child_assess,mother_assess,pie_chart

urlpatterns = [
    path('household/',chwHouseholds,name='household'),
    path('addHousehold/' , addHousehold, name = 'addHousehold'),
    path('edit_household/<int:id>/' , edit_household, name = 'edit_household'),
    path('refer/' , refer, name = 'refer'),
    path('follow_up/',follow_up,name='follow_up'),
    path('delete_ref/<int:id>/',delete_referree,name='delete_ref'),
    path('edit_referral/<int:id>/' , edit_referral, name = 'edit_referral'),
    path('general_assessment/',general_assessment,name='general_assessment'),
    path('child_assess/',child_assess,name='child_assess'),
    path('mother_assess/',mother_assess,name='mother_assess'),
    path('patient_assessments/',assessments,name='patient_assessments'),
    path('charts/', pie_chart, name='charts'),
]

