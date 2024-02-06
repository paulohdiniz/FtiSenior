import os
import django

# Configure as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FitSenior.settings')
django.setup()

import random
from faker import Faker
from django.db import models
from base.models import Customer, ProfissionalSaude

fake = Faker()

# Função para gerar dados fictícios para o modelo Customer
def create_fake_customer():
    return Customer(
        nome=fake.name(),
        email=fake.email(),
        cpf=fake.unique.random_number(digits=11),
        idade=random.randint(18, 80),
        endereco=fake.address(),
        cep=fake.zipcode(),
        pais=fake.country()
    )

# Função para gerar dados fictícios para o modelo ProfissionalSaude
def create_fake_profissional_saude():
    return ProfissionalSaude(
        nome=fake.name(),
        especialidade=fake.job(),
        registro=fake.unique.random_number(digits=6)
    )

# Criar 10 instâncias para o modelo Customer
for _ in range(10):
    fake_customer = create_fake_customer()
    fake_customer.save()

# Criar 10 instâncias para o modelo ProfissionalSaude
for _ in range(10):
    fake_profissional_saude = create_fake_profissional_saude()
    fake_profissional_saude.save()
