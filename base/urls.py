from django.urls import path 
from . import views 

urlpatterns = [ 
	path("", views.home, name="home"), 
	path("ProfissionaisSaude/", views.getAllDoctors),
    path("ProfissionaisSaude/<int:idDoctor>/", views.getDoctorByID),
    path("user/", views.user, name="user"), 
]
