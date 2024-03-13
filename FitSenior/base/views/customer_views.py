from django.shortcuts import render, redirect
from base.models import ProfissionalSaude, Customer

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
	
    return render(request, "profissionaissaude.html",
    {
        'all_doctors': doctor,
	}
      ) 

def user(request): 
	return render(request, "user.html") 