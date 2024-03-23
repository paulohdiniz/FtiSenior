from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    USER_TYPE_CHOICES = (
    (1, 'customer'),
    (2, 'profissionalsaude'),
    (3, 'admin')
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    
    REQUIRED_FIELDS = ['user_type'] # By doing so create superuser command will ask their input

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField(max_length=14, unique=True,null=True)
    idade = models.PositiveIntegerField(null=True)
    endereco = models.CharField(max_length=255,null=True)
    cep = models.CharField(max_length=10,null=True)
    pais = models.CharField(max_length=100,null=True)
    profissionais_saude = models.ManyToManyField('ProfissionalSaude')


    def __str__(self):
        return self.user.username

class ProfissionalSaude(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_acompanhante = models.BooleanField(default=False)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=20, unique=True,null=True)

    def __str__(self):
        return self.user.username
    
class Consulta(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"Consulta {self.local}"

class Chat(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissionais_saude = models.ManyToManyField('ProfissionalSaude')
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=500,null=True)

    def __str__(self):
        return f"Chat {self.local}"
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    profissionais_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)

    def __str__(self):
        return f"Message {self.chat}"
