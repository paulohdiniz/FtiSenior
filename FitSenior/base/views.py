from django.shortcuts import render 

def home(request): 
	return render(request, "home.html") 

def customers(request): 
	return render(request, "customers.html") 

def contact(request): 
	return render(request, "contact.html")
