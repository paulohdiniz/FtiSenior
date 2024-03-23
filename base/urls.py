from django.urls import include, path
from . import views 

urlpatterns = [ 
	path("", views.home, name="home"), 
    path('accounts/', include('django.contrib.auth.urls')), #include /login etc
    path('accounts/signup/doctor/', views.doctor_login, name='doctor_signup'),
    path('accounts/signup/customer/', views.customer_login, name='customer_signup'),
	path("ProfissionaisSaude/", views.getAllDoctors),
    path("ProfissionaisSaude/<int:idDoctor>/", views.getDoctorByID),
    path("user/", views.user, name="user"), 
]
