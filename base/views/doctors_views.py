from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from base.models import ProfissionalSaude, Customer
from ..forms import CustomerSignUpForm, DoctorSignUpForm
from ..models import User

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def getAllDoctors(request): 

	all_doctors = ProfissionalSaude.objects.all()
	return render(request, "profissionaissaude.html",
    {
        'all_doctors': all_doctors,
	}
    ) 

def getDoctorByID(request, idDoctor): 
    all_doctors = ProfissionalSaude.objects.all()

    doctor = ProfissionalSaude.objects.get(pk = idDoctor)
    clineteslinkados = doctor.clientes.values()
	
    return render(request, "profissionaissaude.html",
    {
        'all_doctors': doctor,
	}
    )

def setRelationCustomerDoctor(request, idDoctor):
    return render(request, "profissionaissaude.html")

def user(request): 
	return render(request, "user.html") 