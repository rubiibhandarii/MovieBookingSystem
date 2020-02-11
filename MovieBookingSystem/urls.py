from django.contrib import admin
from django.urls import path
from Cinema.views import views_signup, views_customer, views, views_movies, views_tickets, views_login, views_usertable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login/',views_login.login),
    path('signup',views_signup.create),
    path('movies/',views_movies.movies),
    path('ticket',views_tickets.ticket),
    path('theatres/',views_tickets.theatres),


    path('',views.dashboard),
    path('dashboard/customer/',views_customer.customer),
    path('dashboard/movie/',views_movies.movie),
    path('dashboard/tickets/',views_tickets.tickets),
    path('dashboard/usertable/',views_usertable.user_table),

    path('dashboard/usertable/create',views_usertable.create), #form/function
    path('dashboard/usertable/edit/<int:id>',views_usertable.edit), #table edit
    path('dashboard/usertable/update/<int:id>',views_usertable.update),
    path('dashboard/usertable/delete/<int:id>',views_usertable.delete),
    path('dashboard/usertable/search',views_usertable.search),

    path('dashboard/customer/edit/<int:id>',views_customer.edit),
    path('dashboard/customer/update/<int:id>',views_customer.update),
    path('dashboard/customer/delete/<int:id>',views_customer.delete),
    path('dashboard/customer/search',views_customer.search),

    path('dashboard/movie/edit/<int:id>',views_movies.edit),
    path('dashboard/movie/update/<int:id>',views_movies.update),
    path('dashboard/movie/delete/<int:id>',views_movies.delete),
    path('dashboard/movie/create',views_movies.create),

    path('dashboard/tickets/edit/<int:id>',views_tickets.edit),
    path('dashboard/tickets/update/<int:id>',views_tickets.update),
    path('dashboard/tickets/delete/<int:id>',views_tickets.delete),

    path('entry',views_login.entry),
    path('dashboard/logout',views.logout)


]
