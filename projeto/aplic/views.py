from django.shortcuts import render
from django.views.generic import ListView
from typing import Any
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from aplic.models import Produto, Cliente
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def cliente_login(request):
    if request.method == 'GET':
        return render(request , "login.html")
    else:
        
        
        nome = request.POST.get['nome']
        senha = request.POST.get['password']
        cliente = authenticate(request, nome=nome, password=senha)

        if cliente is not None:
            login(request, cliente)
            messages.success(request, 'Login bem-sucedido!')
            return redirect('pagina_login')
        else:
            messages.error(request, 'As credenciais estão incorretas. Tente novamente.')
       

    return render(request, 'login.html')



def cadastro (request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = Cliente.objects.filter(cpf=cpf).first()

        if user:
            return HttpResponse("Já existe usuario com esse cpf")
        else:
            user = Cliente.objects.filter(username=username).first()

            if user:
                return HttpResponse("Já existe usuario com esse cpf")
        
    
        user = Cliente.objects.create(nome=nome, cpf=cpf, username=username, password=senha)
        user.save()

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

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")