from django.contrib import admin

# Register your models here.
from .models import Customer, ProfissionalSaude, Consulta, Chat, Message, User

admin.site.register(Customer)
admin.site.register(User)
admin.site.register(ProfissionalSaude)
admin.site.register(Consulta)
admin.site.register(Chat)
admin.site.register(Message)

