from django.db import models
from authentication.models import User
from helpers.models import TrackingModel
from uuid import uuid4

class Movimentacoes(TrackingModel):
    id_cliente = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, null=False)
    nome = models.CharField(max_length=255, null=False)
    data = models.DateField(null=False)
    tipoMorango = models.CharField(max_length=255, null=False)
    qtdMorango = models.FloatField(null=False)
    precoCaixaMorango = models.FloatField(null=False)
    vendaMorango = models.IntegerField(null=False)
    observacoes = models.TextField(null=True)
    ativo = models.BooleanField(default=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome