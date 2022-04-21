from django.urls import path
from noteberry.views import MovimentacoesApiView, AlteracaoMovimentacoesApiView, ListVendasApiView, ListComprasApiView
urlpatterns = [
    path('movimentacoes', MovimentacoesApiView.as_view(), name='cadastro_movimentacoes'),
    path('movimentacoes/vendas', ListVendasApiView.as_view(), name='movimentacoes_vendas'),
    path('movimentacoes/compras', ListComprasApiView.as_view(), name='movimentacoes_compras'),
    path('movimentacoes/<str:id_cliente>', AlteracaoMovimentacoesApiView.as_view(), name='alteracao_movimentacoes'),
]