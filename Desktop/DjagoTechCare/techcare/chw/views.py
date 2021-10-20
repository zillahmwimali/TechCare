from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        data={}
        return render(request,'index.htm',data)
    else:
        return redirect("auth_login")
        