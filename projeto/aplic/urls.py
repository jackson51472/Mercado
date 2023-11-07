from django.urls import path
from .views import IndexView, MyView, DetalhesProdutoView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("mine/", MyView.as_view(), name="my-view"),
    path("detalhes/",DetalhesProdutoView.as_view(), name="detalhes")
]