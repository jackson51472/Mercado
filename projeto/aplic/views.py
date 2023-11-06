from typing import Any
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from aplic.models import Produto

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()
        return context

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")