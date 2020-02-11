from django.shortcuts import render, redirect
from Cinema.models import Movies #class
from Cinema.forms import User_Form_Movie
from Cinema.authentication import Authentication

@Authentication.valid_admin
def movie(request):
    limit=3
    page=1
    if request.method=="POST":
        if "next" in request.POST:
            page=(int(request.POST['page'])+1)
        elif "prev" in request.POST:
            page=(int(request.POST['page'])-1)
        tempoffset=page-1
        offset=tempoffset*limit
        movie=Movies.objects.raw("select * from cinema_movies limit 3 offset %s",[offset])
    else:
        movie=Movies.objects.raw("select * from cinema_movies limit 3 offset 0")
    return render (request,"dashboard/movie.html",{'movie':movie, 'page': page})


def movies(request):
    return render(request,'movies.html')

@Authentication.valid_admin
def create(request):
    if request.method=="POST":
      form2=User_Form_Movie(request.POST)
      form2.save()
      return redirect('/dashboard/movie')
    else:
      form2=User_Form_Movie()
    return render(request,'dashboard/movieform.html',{'form2':form2})

@Authentication.valid_admin_id
def edit(request,id):
   movies=Movies.objects.get(m_id=id)
   return render(request,'dashboard/editmovies.html',{'movies':movies})

@Authentication.valid_admin_id
def update(request,id):
    movies=Movies.objects.get(m_id=id)
    form=User_Form_Movie(request.POST,instance=movies)
    form.save()
    return redirect('/dashboard/movie')

@Authentication.valid_admin_id
def delete(request,id):
    movies=Movies.objects.get(m_id=id)
    movies.delete()
    return redirect("/dashboard/movie")
