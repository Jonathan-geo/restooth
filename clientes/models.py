from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
from uuid import uuid4

class Cliente(TrackingModel):
    id_cliente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.CharField(max_length=255)
    rg_cpf = models.CharField(max_length=255, unique=True)
    profissao = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
