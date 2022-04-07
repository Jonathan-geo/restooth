from rest_framework import filters
from clientes.models import Cliente, Endereco, Anamnese
from clientes.serializers import ClienteSerializer, EnderecoSerializer, AnamneseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

########################################
#---->CLIENTE
########################################
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



########################################
#---->ENDERECO
########################################
class EnderecoApiView(ListCreateAPIView):
    serializer_class = EnderecoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields=[            
        'id_cliente',
        'rua',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'cep',
        'complemento',  
    ]
    search_fields=[        
        'rua',
        'numero',
        'bairro',
        'cidade',
        'estado',
        'cep',
    ]
    ordering_fields=['estado']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Endereco.objects.filter(owner=self.request.user)


class AlteracaoEnderecoApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = EnderecoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id_cliente'

    def get_queryset(self):
        return Endereco.objects.filter(owner=self.request.user)



########################################
#---->ANAMNESE
########################################
class AnamneseApiView(ListCreateAPIView):
    serializer_class = AnamneseSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
 
    filterset_fields=[            
        'id_cliente',
    ]
    search_fields=[        
        'id_cliente',
    ]
    ordering_fields=['id_cliente']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Anamnese.objects.filter(owner=self.request.user)


class AlteracaoAnamneseApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnamneseSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id_cliente'

    def get_queryset(self):
        return Anamnese.objects.filter(owner=self.request.user)

