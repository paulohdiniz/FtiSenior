from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Customer(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, db_column='senha')
    cpf = models.CharField(max_length=14, unique=True)
    idade = models.PositiveIntegerField(null=True)
    endereco = models.CharField(max_length=255,null=True)
    cep = models.CharField(max_length=10,null=True)
    pais = models.CharField(max_length=100,null=True)
    profissionais_saude = models.ManyToManyField('ProfissionalSaude', related_name='clientes_associados')

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nome

class ProfissionalSaude(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=20, unique=True,null=True)
    clientes = models.ManyToManyField('Customer', related_name='profissionais_saude_associados')

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"Consulta {self.id}"

class Chat(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    profissionais_saude = models.ManyToManyField('ProfissionalSaude', related_name='chats_associados')
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    local = models.CharField(max_length=500,null=True)

    def __str__(self):
        return f"Chat {self.id}"
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    profissionais_saude = models.ForeignKey('ProfissionalSaude', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)

    def __str__(self):
        return f"Message {self.id}"
