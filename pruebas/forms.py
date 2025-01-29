from django import forms
import calculation
from .models import CalculatorRTC, CalculatorRTP



class FormsRTC(forms.Form):
    rtc= forms.DecimalField(max_digits=6, decimal_places=2)
    current_1= forms.DecimalField(max_digits=10, decimal_places=4)
    current_2= forms.DecimalField(max_digits=10, decimal_places=4)
    rtc_cal= forms.DecimalField(widget=calculation.FormulaInput('current_1/current_2'))
    error_rtc= forms.DecimalField(widget=calculation.FormulaInput('(((rtc*current_2)-current_1)/current_1)*100'))

    def save(self):
        CalculatorRTC.objects.create(
            rtc=self.cleaned_data['rtc'], 
            current_1=self.cleaned_data['current_1'], 
            current_2=self.cleaned_data['current_2'], 
            rtc_cal=self.cleaned_data['rtc_cal'],
            error_rtc=self.cleaned_data['error_rtc'])


class FormsRTP(forms.Form):
    rtp= forms.DecimalField(max_digits=6, decimal_places=2)
    voltage_1= forms.DecimalField(max_digits=10, decimal_places=4)
    voltage_2= forms.DecimalField(max_digits=10, decimal_places=4)
    rtp_cal= forms.DecimalField(widget=calculation.FormulaInput('voltage_1/voltage_2'))
    error_rtc= forms.DecimalField(widget=calculation.FormulaInput('(((rtp*voltage_2)-voltage_1)/voltage_1)*100'))

    def save(self):
        CalculatorRTP.objects.create(
            rtp=self.cleaned_data['rtp'], 
            voltage_1=self.cleaned_data['voltage_1'], 
            voltage_2=self.cleaned_data['voltage_2'],
            rtp_cal=self.cleaned_data['rtp_cal'],
            error_rtc=self.cleaned_data['error_rtc'])