from django.db.models.expressions import Case, When
from django.shortcuts import render,redirect
from chw.models import GeneralAssessment, Households, MotherAssessment,Referral,ChildAssessment
from core.models import User,Chw
from .forms import ChwRegistrationForm
from django.contrib import messages
from django.db.models import Sum
from django.http import JsonResponse
import csv,io
from django.core import mail
from django.core.mail import send_mail
from django.db import IntegrityError
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from techcare.settings import EMAIL_HOST_USER
import json
from django.db.models import Count, Case, When
from django.db.models import Sum, IntegerField
from django.db.models.functions import Cast
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


def group_required(ORGANIZATION):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(users):
        if users.is_authenticated:
            if users.groups.filter(name='ORGANIZATION').exists() :
                return True
            else:
                return False
        return redirect('login')
    return user_passes_test(in_groups)




# @login_required(login_url='login') 
# @group_required('ORGANIZATION')
def calendar(request):
    return render(request,'calendar.html') 




# @login_required(login_url='login')
# @group_required('ORGANIZATION')

def register_chw(request):
    template = "register_chw.html"
    data = Chw.objects.all()
    try:
# prompt is a context variable that can have different values      depending on their context
        prompt = {
            'order' : ' Upload file in this order : First name, last name, email, gender',
            'chws': data
                }
        # GET request returns the value of the data with the specified key.
        if request.method == "GET":
            return render(request, template, prompt)

        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Sorry this is not a csv file,kindly check before you proceed')
            return render(request,template,prompt)
        chw_data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(chw_data_set)
        next(io_string)
        

        chw_csvf = csv.reader(io_string, delimiter=',', quotechar="|")
        data = []
        for firstname,lastname, email, *__ in chw_csvf:
            user = User(username=firstname)
            user.first_name=firstname
            user.last_name=lastname
            user.email=email
            data.append(user)
            user.role=User.CHW
            user.save()
       
        users=User.objects.all().filter(role=2)  # send the email to the recipent    
        for user in users:                                   
            password = User.objects.make_random_password(length = 9, 
                            allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')  
            user.set_password(password)
            user.save(update_fields=['password'])
            chw_name=user.first_name
            chw_email=user.email
            subject = "Thank you for choosing TechCare. We are committed to serving our communities"
            message = " Dear {} , \nWelcome to TechCare app.\nYour entry is {} and password is {}  \nVisit this link to Log In  : techcareapp.herokuapp.com/".format(chw_name,chw_email,password,user.role)
            recipient = chw_email
            send_mail(subject, message,EMAIL_HOST_USER,[recipient])


    except IntegrityError as e: 
        return render(request,"reg_error.html")
    context = {}
    return render(request, template, context)




# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def support(request):
    return render(request,'support.html') 

 
# @login_required(login_url='login')
# @group_required('ORGANIZATION')   
def chw_list(request):
    chws = User.objects.all().filter(role=2)
    return render(request,'chw_list.html',{'chws': chws})


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def edit_chw(request,id):
    chw = User.objects.get(id=id)
    if request.method=='POST':
        form = ChwRegistrationForm(request.POST,instance = chw)
        if form.is_valid():
            form.save()
            return redirect('chw_list')

    else:
        form = ChwRegistrationForm(instance = chw)
    return render(request,'edit_chw.html',{'form':form})        


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def delete_chw(request,id):
    chw = User.objects.get(id = id)
    chw.delete()
    return redirect('chw_list')


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def household_list(request):
    households = Households.objects.all()
    return render(request,'household_list.html',{'households': households})


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def delete_household(request,id):
    household = Households.objects.get(id=id)
    household.delete()
    return redirect('household_list')

# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def totals(request):
    total_chws = Chw.objects.count()
    total_households = Households.objects.count()
    total_referrals = Referral.objects.count()
    f=MotherAssessment.objects.values('how_many')
    infant_mortality_total= sum(item['how_many'] for item in f)
    g=GeneralAssessment.objects.values('number_of_people_living_with_diabilities')
    total_number_of_people_with_disabilities= sum(item['number_of_people_living_with_diabilities'] for item in g)
    p=GeneralAssessment.objects.values('number_of_pregnant_women')
    pregnant_women= sum(item['number_of_pregnant_women'] for item in p)
    v=GeneralAssessment.objects.values('number_of_vaccinated_children')
    vaccinated_children= sum(item['number_of_vaccinated_children'] for item in v)
    n=GeneralAssessment.objects.values('number_of_newborns')
    newborns= sum(item['number_of_newborns'] for item in n)
    c=GeneralAssessment.objects.values('number_of_children_under_5_years_of_age')
    children_under_5_years = sum(item['number_of_children_under_5_years_of_age'] for item in c)

    # MotherAssessment.objects.filter(id=id).annotate(bool_col=Sum(Cast('my_bool_col', IntegerField())))
    data = {"total_chws":total_chws,"total_households":total_households,"total_referrals":total_referrals,"infant_mortality_total":infant_mortality_total,'total_number_of_people_with_disabilities':total_number_of_people_with_disabilities,'pregnant_women':pregnant_women,"vaccinated_children":vaccinated_children,"newborns":newborns,"children_under_5_years":children_under_5_years}

    return render(request,'dashboard.html',data)



# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def referral_list(request):
    referrals = Referral.objects.all()
    return render(request,'referral_list.html',{'referrals': referrals})


   

# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def analytics(request):
    labels = []
    values = []
   
    queryset = GeneralAssessment.objects.values('area').annotate(number_of_people_living_with_diabilities=Sum('number_of_people_living_with_diabilities')).order_by('-number_of_people_living_with_diabilities') 
    for entry in queryset:
        labels.append(entry['area'])
        values.append(entry['number_of_people_living_with_diabilities'])
    data = {
        "labels":labels,
        "values":values,

    }
    return render(request,'analytics.html',data)


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def pregnancy(request):
    labels = []
    values = []
   
    queryset = GeneralAssessment.objects.values('area').annotate(number_of_pregnant_women=Sum('number_of_pregnant_women')).order_by('-number_of_pregnant_women') 
    for entry in queryset:
        labels.append(entry['area'])
        values.append(entry['number_of_pregnant_women'])
    data = {
        "labels":labels,
        "values":values,

    }
    return render(request,'pregnant_analysis.html',data)


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def teen_pregnancy(request):
    labels = []
    values = []
   
    queryset = MotherAssessment.objects.values('age').annotate(number_of_pregnant_women=Sum('number_of_pregnant_women')).order_by('-number_of_pregnant_women') 
    for entry in queryset:
        labels.append(entry['area'])
        values.append(entry['number_of_pregnant_women'])
    data = {
        "labels":labels,
        "values":values,

    }
    return render(request,'teen_pregnancy.html',data)


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def linda_mama(request):

    n = MotherAssessment.objects.filter(do_you_have_Linda_Mama =True)
    area=''
    labels = []

    

    for i in n:
        area=i.area
        labels.append(area)
        values= len(i.area)

    data = {
        "labels":labels,    
        "values":values,

    }
    return render(request,'linda_mama.html',data)


# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def child_vaccination(request):
    labels = []
    values = []

    queryset = GeneralAssessment.objects.values('area').annotate(number_of_vaccinated_children=Sum('number_of_vaccinated_children')).order_by('-number_of_vaccinated_children') 
    for entry in queryset:
        labels.append(entry['area'])
        values.append(entry['number_of_vaccinated_children'])
    data = {
        "labels":labels,
        "values":values,

    }
    return render(request,'vaccinated.html',data)

# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def elderly(request):
    labels = []
    values = []

    queryset = GeneralAssessment.objects.values('area').annotate(number_of_elderly=Sum('number_of_elderly')).order_by('-number_of_elderly') 
    for entry in queryset:
        labels.append(entry['area'])
        values.append(entry['number_of_elderly'])
    data = {
        "labels":labels,
        "values":values,

    }
    return render(request,'elderly.html',data)

# @login_required(login_url='login')
# @group_required('ORGANIZATION')
def infant_mortality(request):
    labels = []
    values = []

    queryset = MotherAssessment.objects.values('area').annotate(how_many=Sum('how_many')).order_by('-how_many') 
    for entry in queryset:
        labels.append(entry['area'])
        values.append(entry['how_many'])
    data = {
        "labels":labels,
        "values":values,

    }
    return render(request,'infant_motality.html',data)




