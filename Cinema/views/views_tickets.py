from django.shortcuts import render, redirect
from Cinema.models import Ticket,Movies #class
from Cinema.forms import User_Form_Ticket

def tickets(request):
    tickets = Ticket.objects.all()
    return render(request,'dashboard/tickets.html',{'tickets':tickets})
    #passing variable

# def ticket(request):
#     return render(request,'ticket.html')


def ticket(request):
    if request.method=="POST":
        form=User_Form_Ticket(request.POST)
        form.save()
        return redirect("/home")
    else:
        movies=Movies.objects.all()
        form=User_Form_Ticket()
    return render(request,'ticket.html',{'form':form,'movies':movies})



def theatres(request):
    return render(request,'theatres.html')
