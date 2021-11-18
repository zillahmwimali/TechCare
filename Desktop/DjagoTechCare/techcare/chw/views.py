from django.shortcuts import render, redirect
from .models import GeneralAssessment, Households, MotherAssessment,Referral,Mother_referral
from .forms import HouseholdRegistrationForm,ReferralAssessmentForm,MotherAssessmentForm,GeneralAssessmentForm,ChildAssessmentForm,MotherReferralForm
from django.contrib import messages
from django.urls import reverse  
from core.models import Chw 
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required


def group_required(CHW):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(users):
        if users.is_authenticated:
            if users.groups.filter(name='CHW').exists() :
                return True
            else:
                return False
        return redirect('login')
    return user_passes_test(in_groups)


# @login_required(login_url='login') 
# @group_required('CHW')
def addHousehold(request):
    if request.method == "POST":
        form = HouseholdRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Successfully registered' +
                             str(Households.contact_person_first_name))
            form.save()
            return redirect('household')
        else:
            print(form.errors)
    else:
        form = HouseholdRegistrationForm()
    return render(request, 'addhousehold.html', {'form': form})


# @login_required(login_url='login') 
# @group_required('CHW')
def chwHouseholds(request):
    households = Households.objects.all()
    return render(request, 'household.html', {'households': households})


# @login_required(login_url='login') 
# @group_required('CHW')
def edit_household(request,id):
    household = Households.objects.get(id=id)
    if request.method=='POST':
        form = HouseholdRegistrationForm(request.POST,instance = household )
        if form.is_valid():
            form.save()
            return redirect('household')

    else:
        form = HouseholdRegistrationForm(instance = household )
        return render(request,'edit_household.html',{'form':form}) 

# @login_required(login_url='login') 
# @group_required('CHW')
def refer(request):
    if request.method == "POST":
        form = ReferralAssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Successfully reffered' + str(Referral.patients_first_name))
            form.save()
            return redirect('mother_assess')
        else:
            print (form.errors)
    else:
        form = ReferralAssessmentForm()
    return render(request,'referral.html',{'form':form})

# @login_required(login_url='login') 
# @group_required('CHW')
def follow_up(request):
    referrees = Referral.objects.all()
    return render(request,'follow_up.html',{'referrees': referrees})



# @login_required(login_url='login') 
# @group_required('CHW')
def delete_referree(request,id):
    referral = Referral.objects.get(id=id) 
    referral.delete()
    return redirect(reverse('follow_up'))



# @login_required(login_url='login') 
# @group_required('CHW')
def edit_referral(request,id):
    referral = Referral.objects.get(id=id)
    if request.method=='POST':
        form = ReferralAssessmentForm(request.POST,instance = referral )
        if form.is_valid():
            form.save()
            return redirect('follow_up')

    else:
        form = ReferralAssessmentForm(instance = referral )
    return render(request,'edit_referral.html',{'form':form}) 


# @login_required(login_url='login') 
# @group_required('CHW')
def general_assess(request):
    if request.method == "POST":
        form = GeneralAssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Completed')
            form.save()
            if GeneralAssessment.do_you_have_any_sick_person_in_this_household==True:
                return redirect('refer')
            else:
                return redirect('mother_assess')
        else:
            print (form.errors)
    else:
        form = GeneralAssessmentForm()
    return render(request,'general.html',{'form':form})



# @login_required(login_url='login') 
# @group_required('CHW')
def child_assess(request):
    if request.method == "POST":
        form = ChildAssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Completed')
            form.save()
            return redirect('household')
        else:
            print (form.errors)
    else:
        form = ChildAssessmentForm()
    return render(request,'child_assess.html',{'form':form})

# @login_required(login_url='login') 
# @group_required('CHW')
def mother_assess(request):
    if request.method == "POST":
        form = MotherAssessmentForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Completed')
            form.save()
            if MotherAssessment.do_you_have_any_complications==True:
                return redirect('refer_mother')
            else:
                return redirect('child_assess')
        else:
            print (form.errors)
    else:
        form = MotherAssessmentForm()
    return render(request,'mother.html',{'form':form})

# @login_required(login_url='login') 
# @group_required('CHW')
def refer_mother(request):
    if request.method == "POST":
        form = MotherReferralForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'SYou have reffered' + str(Mother_referral.mothers_first_name))
            form.save()
            return redirect('child_assess')
        else:
            print (form.errors)
    else:
        form = MotherReferralForm()
    return render(request,'mother_referral.html',{'form':form})

    
def calender(request):
    return render(request,'cal.html')



