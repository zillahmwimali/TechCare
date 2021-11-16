
from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact

def contacts(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)    
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})

# Create your views here.
