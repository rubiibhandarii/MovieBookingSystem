from django.shortcuts import render, redirect
from Cinema.models import Customer #class
from Cinema.forms import User_Form_Customer
from django.http import HttpResponse,JsonResponse


def customer(request):
  if request.method=="POST":
      customer=Customer.objects.raw("select * from customer limit 3 offset 3")
  else:
      customer = Customer.objects.raw("select * from customer limit 3 offset 0")
  return render(request,'dashboard/customer.html',{'customer':customer})
    #passing variable
def search(request):
    customer = Customer.objects.filter(c_email__contains=request.GET['search']).values()
    return JsonResponse(list(customer),safe=False)

def edit(request,id):
   customer=Customer.objects.get(c_id=id)#same id name in model
   return render(request,'dashboard/editcustomer.html',{'customer':customer})

def update(request,id):
    customer=Customer.objects.get(c_id=id)
    form=User_Form_Customer(request.POST,instance=customer)
    form.save()
    return redirect('/dashboard/customer')

def delete(request,id):
    customer=Customer.objects.get(c_id=id)
    customer.delete()
    return redirect("/dashboard/customer")
