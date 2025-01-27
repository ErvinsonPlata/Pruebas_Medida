# Generated by Django 5.1.4 on 2025-01-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebas', '0002_alter_calculatorrtp_voltage_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculatorrtc',
            name='error_rtc',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True, verbose_name='%Error RTC'),
        ),
        migrations.AddField(
            model_name='calculatorrtc',
            name='rtc_cal',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True, verbose_name='RTC Calc'),
        ),
        migrations.AddField(
            model_name='calculatorrtp',
            name='error_rtc',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True, verbose_name='%Error RTP'),
        ),
        migrations.AddField(
            model_name='calculatorrtp',
            name='rtp_cal',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True, verbose_name='RTP Calc'),
        ),
    ]
