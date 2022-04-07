from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente, Endereco, Anamnese


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id_cliente',
            'nome',
            'sobrenome',
            'sexo',
            'data_nascimento',
            'rg_cpf',
            'profissao',
            'telefone',
            'ativo',          
        )

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'id_cliente',
            'rua',
            'numero',
            'bairro',
            'cidade',
            'estado',
            'cep',
            'complemento',          
        )

class AnamneseSerializer(ModelSerializer):
    class Meta:
        model = Anamnese
        fields = (
            'id_cliente',
            'estaTratamentoMedico',
            'tomaMedicamento',
            'temAlergia',
            'esteveInternado',
            'jaDesmaiou',
            'temPressaoAlta',
            'doencaCardiaca',
            'doencaRespiratoria',
            'figado',
            'rins',
            'diabetes',
            'hepatite',
            'doencaGrave',
            'temSangramentoGengiva', 
            'temSensibilidade',
            'temDorDente',
            'observacoesAnamnese',        
        )





#from rest_framework import serializers
#from cadastro_cliente import models


#class CadastroSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = models.Clientes
   #     fields = '__all__'


#class CadastroSerializerName(serializers.ModelSerializer):
 #   class Meta:
  #      model = models.Clientes
   #     #fields = '__all__'
    #    fields = (
     #       'id_cliente',
      #      'nome',
       #     'ativo',
        #)

