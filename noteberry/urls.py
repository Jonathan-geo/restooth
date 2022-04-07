from django.urls import path
from noteberry.views import MovimentacoesApiView, AlteracaoMovimentacoesApiView
urlpatterns = [
    path('movimentacoes', MovimentacoesApiView.as_view(), name='cadastro_movimentacoes'),
    path('movimentacoes/<str:id_cliente>', AlteracaoMovimentacoesApiView.as_view(), name='alteracao_movimentacoes'),
]