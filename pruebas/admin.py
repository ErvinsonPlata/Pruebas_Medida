from django.contrib import admin
from .models import CalculatorRTC, CalculatorRTP




class CalculatorRTCAdmin(admin.ModelAdmin):
    list_display = ('rtc', 'current_1', 'current_2')
    search_fields = ('rtc', 'current_1', 'current_2')
    list_filter = ('rtc', 'current_1', 'current_2')

admin.site.register(CalculatorRTC, CalculatorRTCAdmin)

class CalculatorRTPAdmin(admin.ModelAdmin):
    list_display = ('rtp', 'voltage_1', 'voltage_2')
    search_fields = ('rtp', 'voltage_1', 'voltage_2')
    list_filter = ('rtp', 'voltage_1', 'voltage_2')

admin.site.register(CalculatorRTP, CalculatorRTPAdmin)