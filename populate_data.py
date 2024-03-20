
import os, django
import random
from faker import Faker
from itertools import cycle


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FitSenior.settings")  # Substitua 'seu_projeto' pelo nome do seu projeto Django
django.setup()

from base.models import Customer, ProfissionalSaude, Consulta, Chat, Message

fake = Faker()

# Criação de instâncias de Customer e ProfissionalSaude com dados fictícios
for _ in range(10):  # Altere o número conforme necessário
    customer = Customer(
        nome=fake.name(),
        email=fake.email(),
        cpf=fake.unique.random_number(9, True),
        idade=random.randint(18, 80),
        endereco=fake.address(),
        cep=fake.zipcode(),
        pais=fake.country()
    )
    customer.save()

    profissional_saude = ProfissionalSaude(
        nome=fake.name(),
        especialidade=fake.job(),
        registro=fake.unique.random_number(5, True),
    )
    profissional_saude.save()

# Criação de instâncias de Consulta e Chat com dados fictícios
customers_list = list(Customer.objects.all())
profissionais_saude_list = list(ProfissionalSaude.objects.all())

customer_cycle = cycle(customers_list)
profissional_saude_cycle = cycle(profissionais_saude_list)

for _ in range(10):
    consulta = Consulta(
        customer=next(customer_cycle),
        profissional_saude=next(profissional_saude_cycle),
        data=fake.date_between(start_date='-30d', end_date='today'),
        hora=fake.time(),
        local=fake.address()
    )
    consulta.save()

for _ in range(10):
    chat = Chat(
        customer=next(customer_cycle),
        data=fake.date_between(start_date='-30d', end_date='today'),
        hora=fake.time(),
        local=fake.text(max_nb_chars=500)
    )
    chat.save()

    # Adiciona profissionais aleatórios para cada chat
    chat.profissionais_saude.set([next(profissional_saude_cycle)])
    chat.save()

chat_list = list(Chat.objects.all())
chat_cycle = cycle(chat_list)


for _ in range(100):
    message = Message(
        profissionais_saude=next(profissional_saude_cycle),
        chat=next(chat_cycle),
        data=fake.date_between(start_date='-30d', end_date='today'),
        hora=fake.time(),
        texto=fake.text(max_nb_chars=500)

    )
    message.save()

