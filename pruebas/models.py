from django.db import models

# Create your models here.

class CalculatorRTC(models.Model):
    rtc=models.DecimalField(max_digits=4, decimal_places=0, verbose_name='RTC')
    current_1=models.DecimalField(max_digits=5, decimal_places=4, verbose_name='Corriente 1')
    current_2=models.DecimalField(max_digits=5, decimal_places=4, verbose_name='Corriente 2')

    def __str__(self):
        return str(self.rtc)

class CalculatorRTP(models.Model):
    rtp=models.DecimalField(max_digits=4, decimal_places=0, verbose_name='RTP')
    voltage_1=models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Voltaje 1')
    voltage_2=models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Voltaje 2')

    def __str__(self):
        return str(self.rtp)