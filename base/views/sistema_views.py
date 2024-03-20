from django.shortcuts import render, redirect
from ..forms import SignupForm  
from django.contrib.auth import login
from base.models import ProfissionalSaude, Customer

def home(request):
    first_user = Customer.objects.order_by('id').first()
    doctors = ProfissionalSaude.objects.filter(clientes=first_user)

    return render(request, "home.html", {
        'paciente': first_user,
        'doctors': doctors
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})