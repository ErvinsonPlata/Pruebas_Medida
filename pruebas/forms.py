from django import forms
from .models import CalculatorRTC, CalculatorRTP


class FormsRTC(forms.Form):
    rtc= forms.DecimalField(max_digits=4, decimal_places=0)
    current_1= forms.DecimalField(max_digits=5, decimal_places=4)
    current_2= forms.DecimalField(max_digits=5, decimal_places=4)

    def save(self):
        CalculatorRTC.objects.create(rtc=self.cleaned_data['rtc'], current_1=self.cleaned_data['current_1'], current_2=self.cleaned_data['current_2'])


class FormsRTP(forms.Form):
    rtp= forms.DecimalField(max_digits=4, decimal_places=0)
    voltage_1= forms.DecimalField(max_digits=5, decimal_places=4)
    voltage_2= forms.DecimalField(max_digits=5, decimal_places=4)

    def save(self):
        CalculatorRTP.objects.create(rtp=self.cleaned_data['rtp'], voltage_1=self.cleaned_data['voltage_1'], voltage_2=self.cleaned_data['voltage_2'])