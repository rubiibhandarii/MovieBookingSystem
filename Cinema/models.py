from django.db import models

# Create your models here.
class Customer(models.Model):
    c_id=models.AutoField(auto_created=True,primary_key=True) #auto increment
    c_first_name=models.CharField(max_length=30)
    c_last_name=models.CharField(max_length=30)
    c_email=models.EmailField(max_length=100)
    c_password=models.CharField(max_length=100,default="password")

    # def __int__(self):
    #     return self.c_id #returns customer id in interger

class Movies(models.Model):
    m_id=models.AutoField(auto_created=True,primary_key=True)
    m_movie_name=models.CharField(max_length=50)

    # def __int__(self):
    #     return self.m_id

class Ticket(models.Model):
    t_id=models.AutoField(auto_created=True,primary_key=True)
    t_tickets=models.IntegerField(blank=False)
    t_theatres=models.CharField(max_length=50)
    t_seat_type=models.CharField(max_length=30)
    t_hall=models.CharField(max_length=50)
    cus_id= models.CharField(max_length=50)
    mov_id= models.CharField(max_length=50)
    # cus_id= models.ForeignKey(Customer, on_delete=models.CASCADE)
    # mov_id= models.ForeignKey(Movies, on_delete=models.CASCADE)

class User(models.Model):
    u_id=models.AutoField(auto_created=True,primary_key=True) #auto increment
    u_email=models.EmailField(max_length=100)
    u_password=models.CharField(max_length=100)

    class Meta:
        #data of data
        db_table="customer"
        db_table="movies"
        db_table="tickets"
        db_table="user"
