from django.urls import path
from .views import child_assess,calender, chwHouseholds,addHousehold,edit_household,general_assess,refer,follow_up,delete_referree,edit_referral,child_assess,mother_assess,refer_mother

urlpatterns = [
    path('household/',chwHouseholds,name='household'),
    path('addHousehold/' , addHousehold, name = 'addHousehold'),
    path('edit_household/<int:id>/' , edit_household, name = 'edit_household'),
    path('refer/' , refer, name = 'refer'),
    path('follow_up/',follow_up,name='follow_up'),
    path('delete_ref/<int:id>/',delete_referree,name='delete_ref'),
    path('edit_referral/<int:id>/' , edit_referral, name = 'edit_referral'),
    path('general_assessment/',general_assess,name='general_assessment'),
    path('child_assess/',child_assess,name='child_assess'),
    path('mother_assess/',mother_assess,name='mother_assess'),
    path('refer_mother/',refer_mother,name='refer_mother'),
    path('cal/' , calender, name = 'cal'),


]

