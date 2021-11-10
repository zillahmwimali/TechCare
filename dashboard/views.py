from django.shortcuts import render,redirect
from chw.models import Chw, Households,Referral
from .forms import ChwRegistrationForm, EditProfileForm
from django.contrib import messages
from django.db.models import Sum
from django.http import JsonResponse
from .models import OrgProfile


def calendar(request):
    return render(request,'calendar.html') 

def register_chw(request):
    if request.method == "POST":
        form = ChwRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,'Successfully registered' + str(Chw.first_name))
            form.save()
            return redirect('chw_list')
        else:
            print (form.errors)
    else:
        form = ChwRegistrationForm()
    return render(request,'register_chw.html',{'form':form})


def chw_list(request):
    chws = Chw.objects.all()
    return render(request,'chw_list.html',{'chws': chws})


def edit_chw(request,id):
    chw = Chw.objects.get(id=id)
    if request.method=='POST':
        form = ChwRegistrationForm(request.POST,instance = chw)
        if form.is_valid():
            form.save()
            return redirect('chw_list')

    else:
        form = ChwRegistrationForm(instance = chw)
        return render(request,'edit_chw.html',{'form':form})        


def delete_chw(request,id):
    chw = Chw.objects.get(id=id)
    chw.delete()
    return redirect('chw : chw_list')


def household_list(request):
    households = Households.objects.all()
    return render(request,'household_list.html',{'households': households})


def delete_household(request,id):
    household = Households.objects.get(id=id)
    household.delete()
    return redirect('household_list')

def totals(request):
    total_chws = Chw.objects.count()
    total_households = Households.objects.count()
    total_referrals = Referral.objects.count()
    data = {"total_chws":total_chws,"total_households":total_households,"total_referrals":total_referrals}

    return render(request,'dashboard.html',data)


def referral_list(request):
    referrals = Referral.objects.all()
    return render(request,'referral_list.html',{'referrals': referrals})

def edit_profile(request):
    if request.method=="POST":
        forms=EditProfileForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            
            return redirect("dashboard")
        else:
            print(forms.errors)

    else:
        forms=EditProfileForm()
    return render(request,"edit_profile.html",{"form":forms})

