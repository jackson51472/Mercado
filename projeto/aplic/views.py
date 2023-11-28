from django.shortcuts import render
from django.views.generic import ListView
from typing import Any
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from aplic.models import Produto, Cliente, User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.models import Q

def buscar_produtos(request):
    termo_de_busca = request.GET.get('search')

    if termo_de_busca:
        resultados = Produto.objects.filter(Q(nome_produto__icontains=termo_de_busca))
    else:
        resultados = Produto.objects.all()

    context = {'resultados': resultados, 'termo_de_busca': termo_de_busca}
    return render(request, 'buscar.html', context)

def cliente_login(request):
    if request.method == 'POST':
    
        # Pega o nome e passaword do login.html, através da tag name no input.
        nome = request.POST.get['nome']
        senha = request.POST.get['password']
        #===============================================================


        # Verifica os campos
        cliente = authenticate(request, username=nome, password=senha)


        # Se cliente não tiver autenticado ira retornar None e não ira logar
        if cliente is not None:         
            login(request, cliente)
            return redirect('/index')
        
       
       

    return render(request, 'login.html')

def cadastro (request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        # Pega o nome e passaword do cadastro.html, através da tag name no input.
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        
        username = request.POST.get('username')
        password = request.POST.get('senha')

        # Verifica se o CPF já existe no sistema, caso exista a conta não poderá ser criada
        cliente = Cliente.objects.filter(cpf=cpf).first()

        if cliente:
            return HttpResponse("Já existe usuario com esse cpf")
        
        # Primeiro cria o User com os atributos username e password.
        # Caso seu User tenha e-mail basta apenas criar "email=request.POST.get("email")",
        # mas para isso deve ter um input na pagina de cadastro
        user = User.objects.create_user(username=username, password=password)
       
        # Cria o Cliente, nele passa o User que ele ira pertencer.
        # Mas para seu Cliente.models deve ter "user=models.OneToOneField(User, on_delete=models.CASCADE)" 
        # Caso não esteja criado basta ir em models e ver oque foi feito
        cliente = Cliente.objects.create(nome=nome, cpf=cpf, user=user)
        cliente.save()

        return HttpResponse("Cadastrado")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context

class DetalhesProdutoView(ListView):
    template_name = 'detalhe_produto.html'
    paginate_by = 5
    ordering = 'nome_produto'
    model = Produto

    def get_context_data(self, **kwargs: Any):
        context = super(DetalhesProdutoView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['produto'] = Produto.objects.filter(id=id).first
        return context

