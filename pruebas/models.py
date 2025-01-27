from django.db import models

# Create your models here.

class CalculatorRTC(models.Model):
    rtc=models.DecimalField(max_digits=4, decimal_places=2, verbose_name='RTC')
    current_1=models.DecimalField(max_digits=5, decimal_places=4, verbose_name='Corriente 1')
    current_2=models.DecimalField(max_digits=5, decimal_places=4, verbose_name='Corriente 2')
    rtc_cal=models.DecimalField(max_digits=5, decimal_places=4,null=True, verbose_name='RTC Calc')
    error_rtc=models.DecimalField(max_digits=5, decimal_places=4, null=True, verbose_name='%Error RTC')



    def __str__(self):
        return str(self.rtc)

class CalculatorRTP(models.Model):
    rtp=models.DecimalField(max_digits=4, decimal_places=0, verbose_name='RTP')
    voltage_1=models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Voltaje 1')
    voltage_2=models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Voltaje 2')
    rtp_cal=models.DecimalField(max_digits=5, decimal_places=4,null=True, verbose_name='RTP Calc')
    error_rtc=models.DecimalField(max_digits=5, decimal_places=4,null=True, verbose_name='%Error RTP')

    def __str__(self):
        return str(self.rtp)