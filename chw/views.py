from django.shortcuts import render, redirect
from .models import Households,Referral
from .forms import HouseholdRegistrationForm,ReferralRegistrationForm
from django.contrib import messages
from django.urls import reverse             



# def pie_chart(request):
#     labels = []
#     data = []

#     queryset = Households.objects.order_by('household_area')[:5]
#     for household in queryset:
#         labels.append(Households.phone_number)
#         data.append(Households.number_of_newborns)

#     return render(request, 'analytics.html', {
#         'labels': labels,
#         'data': data,
#     })

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


def chwHouseholds(request):
    households = Households.objects.all()
    return render(request, 'household.html', {'households': households})


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
def refer(request):

    if request.method == "POST":
        form = ReferralRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Successfully reffered' + str(Referral.patients_first_name))
            form.save()
            return redirect('follow_up')
        else:
            print (form.errors)
    else:
        form = ReferralRegistrationForm()
    return render(request,'referral.html',{'form':form})

def follow_up(request):
    referrees = Referral.objects.all()
    return render(request,'follow_up.html',{'referrees': referrees})


def delete_referree(request,id):
    referral = Referral.objects.get(id=id)
    referral.delete()
    return redirect(reverse('follow_up'))



def edit_referral(request,id):
    referral = Referral.objects.get(id=id)
    if request.method=='POST':
        form = ReferralRegistrationForm(request.POST,instance = referral )
        if form.is_valid():
            form.save()
            return redirect('follow_up')

    else:
        form = ReferralRegistrationForm(instance = referral )
    return render(request,'edit_referral.html',{'form':form}) 



def assessments(request):
    return render(request, 'patient_assessments.html')


def referrals(request):
    return render(request, 'Referrals.html')


def followUp(request):
    return render(request, 'follow-up.html')

def new_household(request):
    return render(request, 'new_household.html')

def general_assessment(request):
    return render(request,'general_assessment.html')

def child_assess(request):
    return render(request,'child_assess.html')


def mother_assess(request):
    return render(request,'mother_assess.html')