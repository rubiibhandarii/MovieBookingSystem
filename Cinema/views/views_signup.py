from django.shortcuts import render, redirect
from Cinema.models import Customer
from Cinema.forms import User_Form_Customer

def create(request):
    if request.method=="POST":
        request.session['Session_c_email']=request.POST['c_email']

        form = User_Form_Customer(request.POST)
        form.save()
        request.session['book_allow']=1
        return redirect("/ticket")
    else:
        form = User_Form_Customer()
    return render(request,"signup.html",{'form':form})
