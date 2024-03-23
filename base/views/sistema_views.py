from django.shortcuts import render, redirect
from django.contrib.auth import login
from base.models import ProfissionalSaude, Customer

def home(request):
    first_user = Customer.objects.order_by('user_id').first()
    doctors_of_first_user = first_user.profissionais_saude.all()
    return render(request, "home.html", {
        'paciente': first_user    
    })


def doctor_login(request):
    return render(request, "login.html")

def customer_login(request):
    return render(request, "login.html")
