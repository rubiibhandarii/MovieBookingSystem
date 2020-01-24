from django.shortcuts import render, redirect

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def home(request):
    return render(request,'home.html')
