
from django.conf.urls import url
from . import views

app_name='event'
urlpatterns=[

   url('myCalender/', views.CalendarView.as_view(), name='calendar'), 
]
