from django.shortcuts import render, redirect
from Cinema.authentication import Authentication

@Authentication.valid_admin
def dashboard(request):
    return render(request,'dashboard/dashboard.html')


def home(request):
    return render(request,'home.html')

def logout(request):
    request.session['u_password']=""
    return redirect("/")
