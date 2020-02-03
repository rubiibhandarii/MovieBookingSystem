from django.shortcuts import render,redirect
from Cinema.models import User
from django.db.models import Q
from django.contrib import messages

class Authentication:
    def valid_admin(function):
        def validation(request):
            try:
                user = User.objects.get(Q(u_email=request.session['u_email']) & Q(u_password=request.session['u_password']))
                return function(request)
            except:
                messages.warning(request,"Please login first!")
                return redirect ("/login")
        return validation

    def valid_admin_id(function):
        def validation(request,id):
            try:
                user = User.objects.get(Q(u_email=request.session['u_email']) & Q(u_password=request.session['u_password']))
                return function(request,id)
            except:
                messages.warning(request,"Do login first!")
                return redirect ("/login")
        return validation
