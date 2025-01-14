from django.urls import path
from pruebas.views import StartList
from .views import FormsRTCView, FormsRTPView


urlpatterns = [
    path("start/",StartList.as_view(), name="start"),
    path("RTC/", FormsRTCView.as_view(), name="RTC"),
    path("RTP/", FormsRTPView.as_view(), name="RTP"),


]