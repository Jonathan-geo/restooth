from rest_framework import filters
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class ClienteApiView(ListCreateAPIView):
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields=['id_cliente', 'ativo', 'nome', 'rg_cpf', 'profissao', 'sexo']
    search_fields=['ativo', 'nome', 'profissao', 'sexo']
    ordering_fields=['nome']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Cliente.objects.filter(owner=self.request.user)


class AlteracaoClienteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id_cliente'

    def get_queryset(self):
        return Cliente.objects.filter(owner=self.request.user)