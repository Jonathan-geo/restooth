from rest_framework.serializers import ModelSerializer
from noteberry.models import Movimentacoes


class MovimentacoesSerializer(ModelSerializer):
    class Meta:
        model = Movimentacoes
        fields = (
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        )