from rest_framework import filters
from noteberry.models import Movimentacoes
from noteberry.serializers import MovimentacoesSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

########################################
#---->MOVIMENTACOES
########################################
class MovimentacoesApiView(ListCreateAPIView):
    serializer_class = MovimentacoesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields=[
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        ]
    search_fields=[
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        ]
    ordering_fields=['nome']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Movimentacoes.objects.filter(owner=self.request.user)


class AlteracaoMovimentacoesApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovimentacoesSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id_cliente'

    def get_queryset(self):
        return Movimentacoes.objects.filter(owner=self.request.user)


########################################
#---->MOVIMENTACOES.VENDAS
########################################
class ListVendasApiView(ListAPIView):
    serializer_class = MovimentacoesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields=[
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        ]
    search_fields=[
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        ]
    ordering_fields=['nome']

    def get_queryset(self):
        return Movimentacoes.objects.filter(owner=self.request.user, vendaMorango=1)


########################################
#---->MOVIMENTACOES.COMPRAS
########################################
class ListComprasApiView(ListAPIView):
    serializer_class = MovimentacoesSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields=[
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        ]
    search_fields=[
            'id_cliente',
            'nome',
            'data',
            'tipoMorango',
            'qtdMorango',
            'precoCaixaMorango',
            'vendaMorango',
            'observacoes',
            'ativo',
        ]
    ordering_fields=['nome']

    def get_queryset(self):
        return Movimentacoes.objects.filter(owner=self.request.user, vendaMorango=0)






# class CreateAtividadeAPIView(CreateAPIView):
#     serializer_class = AtividadeSerializer
#     permission_classes = (IsAuthenticated,)

#     def perform_create(self, serializer):
#         return serializer.save(usuario=self.request.user)



# class ListAtividadesAPIView(ListAPIView):
#     serializer_class = AtividadeSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         return Atividade.objects.filter(usuario=self.request.user)
