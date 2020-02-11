from django.shortcuts import render, redirect
from Cinema.models import Ticket,Movies #class
from Cinema.forms import User_Form_Ticket
from Cinema.authentication import Authentication

@Authentication.valid_admin
def tickets(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        tickets=Ticket.objects.raw("select * from cinema_ticket limit 3 offset %s",[offset])
    else:
        tickets=Ticket.objects.raw("select * from cinema_ticket limit 3 offset 0")
    return render (request,"dashboard/tickets.html",{'tickets':tickets, 'page': page})


def ticket(request):
    if request.method=="POST":
        form=User_Form_Ticket(request.POST)
        form.save()
        del request.session['book_allow']
        del request.session['Session_c_email']
        return redirect("/home")
    else:
        movies=Movies.objects.all()
        form=User_Form_Ticket()
    return render(request,'ticket.html',{'form':form,'movies':movies})


def theatres(request):
    return render(request,'theatres.html')

@Authentication.valid_admin_id
def edit(request,id):
    movie=Movies.objects.all()
    tickets=Ticket.objects.get(t_id=id)
    return render(request,'dashboard/editticket.html',{'tickets':tickets,'movie':movie})

@Authentication.valid_admin_id
def update(request,id):
    tickets=Ticket.objects.get(t_id=id)
    form=User_Form_Ticket(request.POST,instance=tickets)
    form.save()
    return redirect('/dashboard/tickets')

@Authentication.valid_admin_id
def delete(request,id):
    tickets=Ticket.objects.get(t_id=id)
    tickets.delete()
    return redirect("/dashboard/tickets")
