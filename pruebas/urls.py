from django.urls import path
from pruebas.views import StartList

urlpatterns = [
    path("start/",StartList.as_view(), name="start"),

]