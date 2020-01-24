from django.shortcuts import render, redirect
from Cinema.forms import User_Form
from Cinema.models import User

def user_table(request):
    users=User.objects.all()
    return render(request,'dashboard/usertable.html',{'users':users})

def create(request):
    if request.method=="POST":
      form=User_Form(request.POST)
      form.save()
      return redirect('/dashboard/usertable')
    else:
      form = User_Form() #class in form
    return render(request,'dashboard/userform.html',{'form':form})

def edit (request,id):
   users=User.objects.get(u_id=id)
   return render(request,'dashboard/edituser.html',{'users':users})

def update(request,id):
     users=User.objects.get(u_id=id)
     form=User_Form(request.POST,instance=users)
     # return User_Form(request.POST,"update.html",instance=user)#update user ie already initialed
     form.save()
     return redirect('/dashboard/usertable')

def delete(request,id):
    users=User.objects.get(u_id=id)
    users.delete()
    return redirect("/dashboard/usertable")
