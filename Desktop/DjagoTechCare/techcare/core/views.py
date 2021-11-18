from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic.edit import FormView
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django.urls import reverse_lazy
from django.contrib import messages
import csv,io
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.db import IntegrityError
from techcare.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login
from.models import OrgProfile



def home(request):
    return render(request,'try.html')


def doc(request):
    return render(request,'doc.html')

class LoginView(FormView):
    """login view"""
    form_class = forms.LoginForm
    success_url = reverse_lazy('change_password')
    template_name = 'login.html'
    
    
    @csrf_exempt
    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],password=credentials['password'])

        if user is not None:
            login(self.request, user)
            if user.is_previously_logged_in==False:
                return HttpResponseRedirect(reverse_lazy('change_password'))
                
            else:
                if user.role==1:
                    print(user.role)
                    return HttpResponseRedirect(reverse_lazy('dashboard'))
                elif user.role==2:
                    return HttpResponseRedirect(reverse_lazy('households'))
            
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
        return HttpResponseRedirect(reverse_lazy('login'))

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            user.is_previously_logged_in=True
            user.save()
            if user.role==1:
                return HttpResponseRedirect(reverse_lazy('dashboard'))
            elif user.role==2:
                return HttpResponseRedirect(reverse_lazy('households'))
            
        else:
            print(form.errors)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})

def org_list(request):
    orgs = User.objects.all().filter(role=1)
    return render(request,'org_list.html',{'orgs': orgs})

def register_organization(request):
    template = "organization.html"
    data = OrgProfile.objects.all()
    try:
# prompt is a context variable that can have different values      depending on their context
        prompt = {
            'order' : ' Upload file in this order : Organization name, email, membership number',
            'orgs': data
                }
        # GET request returns the value of the data with the specified key.
        if request.method == "GET":
            return render(request, template, prompt)

        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Sorry this is not a csv file,kindly check before you proceed')
            return render(request,template,prompt)
        org_data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(org_data_set)
        next(io_string)
        

        org_csvf = csv.reader(io_string, delimiter=',', quotechar="|")
        data = []
        for firstname, email, *__ in org_csvf:
            user = User(username=firstname)
            user.first_name=firstname
            user.email=email
            data.append(user)
            user.role=User.ORGANIZATION
            user.save()
       
        users=User.objects.all().filter(role=1)  # send the email to the recipent    
        for user in users:                                   
            password = User.objects.make_random_password(length = 9, 
                            allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')  
            user.set_password(password)
            user.save(update_fields=['password'])
            org_name=user.first_name
            org_email=user.email
            subject = "Thank you for choosing TechCare. We are committed to serving our communities"
            message = " Dear {} , \nWelcome to TechCare app.\nYour entry is {} and password is {}  \nVisit this link to Log In  : techcareapp.herokuapp.com/".format(org_name,org_email,password,user.role)
            recipient = org_email
            send_mail(subject, message,EMAIL_HOST_USER,[recipient])


    except IntegrityError as e: 
        return render(request,"reg_error.html")
    context = {}
    return render(request, template, context)