from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse


# Create your views here.
class StartList(TemplateView):  # vista basada en clases
    template_name = 'pruebas/start.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Pruebas'
        return context 