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


class Endereco(TrackingModel):
    id_cliente = models.CharField(max_length=255, unique=True)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cliente


class Anamnese(TrackingModel):
    id_cliente = models.CharField(max_length=255, unique=True)
    estaTratamentoMedico = models.BooleanField(default=False)
    tomaMedicamento = models.BooleanField(default=False)
    temAlergia = models.BooleanField(default=False)
    esteveInternado = models.BooleanField(default=False)
    jaDesmaiou = models.BooleanField(default=False)
    temPressaoAlta = models.BooleanField(default=False)
    doencaCardiaca = models.BooleanField(default=False)
    doencaRespiratoria = models.BooleanField(default=False)
    figado = models.BooleanField(default=False)
    rins = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hepatite = models.BooleanField(default=False)
    doencaGrave = models.BooleanField(default=False)
    temSangramentoGengiva = models.BooleanField(default=False) 
    temSensibilidade = models.BooleanField(default=False)
    temDorDente = models.BooleanField(default=False)
    observacoesAnamnese = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cliente





