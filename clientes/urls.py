from django.urls import path
from clientes.views import ClienteApiView, AlteracaoClienteApiView, EnderecoApiView, AlteracaoEnderecoApiView, AnamneseApiView, AlteracaoAnamneseApiView

urlpatterns = [
    path('cliente', ClienteApiView.as_view(), name='clientes'),
    path('cliente/<str:id_cliente>', AlteracaoClienteApiView.as_view(), name='alteracao_clientes'),

    path('endereco', EnderecoApiView.as_view(), name='endereco'),
    path('endereco/<str:id_cliente>', AlteracaoEnderecoApiView.as_view(), name='alteracao_endereco'),

    path('anamnese', AnamneseApiView.as_view(), name='anamnese'),
    path('anamnese/<str:id_cliente>', AlteracaoAnamneseApiView.as_view(), name='alteracao_anamnese'),
]