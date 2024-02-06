from django.db import models

class Customer(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    idade = models.PositiveIntegerField()
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)
    profissionais_saude = models.ManyToManyField('ProfissionalSaude', related_name='clientes_associados')

    def __str__(self):
        return self.nome

class ProfissionalSaude(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=20, unique=True)
    clientes = models.ManyToManyField(Customer, related_name='profissionais_saude_associados')

    def __str__(self):
        return self.nome
