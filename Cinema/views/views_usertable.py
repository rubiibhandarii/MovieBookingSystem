from django.shortcuts import render, redirect
from Cinema.forms import User_Form
from Cinema.models import User
from Cinema.authentication import Authentication

@Authentication.valid_admin
def search(request):
    user = User.objects.filter(u_email__contains=request.GET['search']).values()
    return JsonResponse(list(user),safe=False)

@Authentication.valid_admin
def user_table(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        users=User.objects.raw("select * from user limit 3 offset %s",[offset])
    else:
        users=User.objects.raw("select * from user limit 3 offset 0")
    return render (request,"dashboard/usertable.html",{'users':users, 'page': page})


def create(request):
    if request.method=="POST":
      form=User_Form(request.POST)
      form.save()
      return redirect('/dashboard/usertable')
    else:
      form = User_Form() #class in form
    return render(request,'dashboard/userform.html',{'form':form})

@Authentication.valid_admin_id
def edit (request,id):
   users=User.objects.get(u_id=id)
   return render(request,'dashboard/edituser.html',{'users':users})

@Authentication.valid_admin_id
def update(request,id):
     users=User.objects.get(u_id=id)
     form=User_Form(request.POST,instance=users)
     # return User_Form(request.POST,"update.html",instance=user)#update user ie already initialed
     form.save()
     return redirect('/dashboard/usertable')

@Authentication.valid_admin_id
def delete(request,id):
    users=User.objects.get(u_id=id)
    users.delete()
    return redirect("/dashboard/usertable")
