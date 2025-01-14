from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from .forms import FormsRTC, FormsRTP
from .models import CalculatorRTC, CalculatorRTP


# Create your views here.
class StartList(TemplateView):  # vista basada en clases
    template_name = 'pruebas/start.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Pruebas'
        return context 
    

class FormsRTCView(generic.FormView):
    template_name = 'pruebas/rtc.html'
    form_class = FormsRTC
    success_url = reverse_lazy("start")

    def form_valid(self, form):  # guardas los datos en la base de datos
        form.save()
        return super().form_valid(form)

class FormsRTPView(generic.FormView):
    template_name = 'pruebas/rtp.html'
    form_class = FormsRTP
    success_url = reverse_lazy("start")

    def form_valid(self, form):  # guardas los datos en la base de datos
        form.save()
        return super().form_valid(form)