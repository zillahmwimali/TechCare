from django.urls import path
from .views import home,LoginView,register_organization,change_password,doc

urlpatterns = [
    path('',home, name='home'),
    path('organization/',register_organization, name='organization'),
    path('login/',LoginView.as_view(),name='login'),
    path('change_password/',change_password,name='change_password'),
    path('doc/',doc, name='doc'),


]