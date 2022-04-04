from django.urls import path
from clientes.views import ClienteApiView, AlteracaoClienteApiView

urlpatterns = [
    path('', ClienteApiView.as_view(), name='clientes'),
    path('<str:id_cliente>', AlteracaoClienteApiView.as_view(), name='alteracao_clientes'),
]