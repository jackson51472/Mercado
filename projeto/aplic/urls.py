from django.urls import path
from .views import IndexView, MyView, DetalhesProdutoView, cadastro, cliente_login

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("mine/", MyView.as_view(), name="my-view"),
    path("detalhes/<int:id>",DetalhesProdutoView.as_view(), name="detalhe_produto"),
    path("login/", cliente_login, name="login"),
    path("cadastro/", cadastro, name="cadastro")
]