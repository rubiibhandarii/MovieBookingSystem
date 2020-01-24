from django.shortcuts import render, redirect
from Cinema.models import Movies #class
from Cinema.forms import User_Form_Movie

def movie(request):
    movie = Movies.objects.all()
    return render(request,'dashboard/movie.html',{'movie':movie})
    #passing variable

def movies(request):
    return render(request,'movies.html')

def create(request):
    if request.method=="POST":
      form2=User_Form_Movie(request.POST)
      form2.save()
      return redirect('/dashboard/movie')
    else:
      form2=User_Form_Movie()
    return render(request,'dashboard/movieform.html',{'form2':form2})


def edit(request,id):
   movies=Movies.objects.get(m_id=id)
   return render(request,'dashboard/editmovies.html',{'movies':movies})

def update(request,id):
    movies=Movies.objects.get(m_id=id)
    form=User_Form_Movie(request.POST,instance=movies)
    form.save()
    return redirect('/dashboard/movie')

def delete(request,id):
    movies=Movies.objects.get(m_id=id)
    movies.delete()
    return redirect("/dashboard/movie")
