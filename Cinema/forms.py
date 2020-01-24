from django import forms
from Cinema.models import User, Customer,Ticket,Movies

class User_Form(forms.ModelForm):
    u_email=forms.CharField(widget=forms.TextInput(
    attrs={
         'class': 'form-control',
         'placeholder':'Enter your email'
    }))

    u_password=forms.CharField(widget=forms.PasswordInput(
    attrs={
         'class' : 'form-control',
         'placeholder' : 'Enter your password'
    }))


    class Meta:
        model=User
        fields="__all__"

class User_Form_Customer(forms.ModelForm):

    c_first_name = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'First name'
    }
    ))

    c_last_name = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Last name'
    }
    ))

    c_email = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Enter your email'
    }
    ))
    c_password = forms.CharField(widget=forms.PasswordInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Enter your password'
    }
    ))

    class Meta:
        model = Customer
        fields="__all__"

class User_Form_Ticket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields="__all__"

class User_Form_Movie(forms.ModelForm):

    m_movie_name = forms.CharField(widget=forms.TextInput(
    attrs={
            'class' : 'form-control',
            'placeholder':'Movie name'
    }
    ))
    class Meta:
        model = Movies
        fields="__all__"
