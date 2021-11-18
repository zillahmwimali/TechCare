from django.urls import path
from .views import totals
from .views import register_chw,chw_list,edit_chw,delete_chw,calendar,household_list,delete_household,referral_list,analytics,support,teen_pregnancy,linda_mama,child_vaccination,elderly,infant_mortality


urlpatterns = [

    path('dashboard/',totals, name='dashboard'),
    path('calendar/',calendar, name='calendar'),
    path('register_chw/',register_chw, name= 'register_chw'),
    path('chw_list/',chw_list, name = 'chw_list'),
    path('household_list/',household_list, name = 'household_list'),
    path('edit_chw/<int:id>/',edit_chw,name='edit_chw'),
    path('delete_chw/<int:id>/',delete_chw,name='delete_chw'),
    path('delete_household/<int:id>/',delete_household,name='delete_household'),
    path('referral_list/',referral_list, name = 'referral_list'),
    path('analytics/',analytics, name='analytics'),\
    path('support/',support, name='support'),
    path('teen_pregnancy/',teen_pregnancy, name='teen_pregnancy'),
    path('linda_mama/',linda_mama, name='linda_mama'),
    path('vaccination/',child_vaccination, name='vaccination'),
    path('elderly/',elderly, name='elderly'),
    path('infant_mortality/',infant_mortality, name='infant_mortality'),


]