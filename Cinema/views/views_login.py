from django.shortcuts import render, redirect
from Cinema.models import User
from Cinema.authentication import Authentication

def login(request):
    user=User.objects.all()
    return render(request,'login.html',{'user':user})

def entry(request):
    request.session['u_email']=request.POST['u_email']
    request.session['u_password']=request.POST['u_password']
    return redirect("/")
