from django.urls import path
from .views import IndexView, DetalhesProdutoView,buscar_produtos, cadastro, cliente_login
from django.contrib.auth import views
from aplic.forms import UserLoginForm



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
   path('buscar_produtos/', buscar_produtos, name='buscar_produtos'),
    path("detalhes/<int:id>",DetalhesProdutoView.as_view(), name="detalhe_produto"),
    #path("login/", cliente_login, name="login"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path("cadastro/", cadastro, name="cadastro")
]