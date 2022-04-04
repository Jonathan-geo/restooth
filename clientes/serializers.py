from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente


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

