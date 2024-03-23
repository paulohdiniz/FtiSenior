from django.shortcuts import render, redirect
from django.contrib.auth import login
from base.models import ProfissionalSaude, Customer

def home(request):
    first_user = Customer.objects.order_by('id').first()
    doctors = ProfissionalSaude.objects.filter(clientes=first_user)

    return render(request, "home.html", {
        'paciente': first_user,
        'doctors': doctors
    })


def doctor_login(request):
    return render(request, "login.html")

def customer_login(request):
    return render(request, "login.html")
