from django.contrib import admin

# Register your models here.
from .models import Customer, ProfissionalSaude 

admin.site.register(Customer)
admin.site.register(ProfissionalSaude)

