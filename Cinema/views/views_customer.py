from django.shortcuts import render, redirect
from Cinema.models import Customer #class
from Cinema.forms import User_Form_Customer
from django.http import HttpResponse,JsonResponse
from Cinema.authentication import Authentication

@Authentication.valid_admin
def customer(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        customer=Customer.objects.raw("select * from cinema_customer limit 3 offset %s",[offset])
    else:
        customer=Customer.objects.raw("select * from cinema_customer limit 3 offset 0")
    return render (request,"dashboard/customer.html",{'customer':customer, 'page': page})

@Authentication.valid_admin
def search(request):
    customer = Customer.objects.filter(c_email__contains=request.GET['search']).values()
    return JsonResponse(list(customer),safe=False)

@Authentication.valid_admin_id
def edit(request,id):
   customer=Customer.objects.get(c_id=id)#same id name in model
   return render(request,'dashboard/editcustomer.html',{'customer':customer})

@Authentication.valid_admin_id
def update(request,id):
    customer=Customer.objects.get(c_id=id)
    form=User_Form_Customer(request.POST,instance=customer)
    form.save()
    return redirect('/dashboard/customer')

@Authentication.valid_admin_id
def delete(request,id):
    customer=Customer.objects.get(c_id=id)
    customer.delete()
    return redirect("/dashboard/customer")
