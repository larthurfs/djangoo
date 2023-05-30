from django.contrib import admin
from django.urls import path

from apps.core.views import home, ferramenta_converter_pdf_para_word, ferramenta_youtube, ferramenta_qrcode, ferramenta_senha, ferramenta_numeros, ferramenta_recibos

urlpatterns = [
    path('', home, name='home'),
    path('pdfword', ferramenta_converter_pdf_para_word, name='ferramenta_converter_pdf_para_word'),
    path('youtube', ferramenta_youtube, name='ferramenta_youtube'),
    path('qrcode', ferramenta_qrcode, name='ferramenta_qrcode'),
    path('senha', ferramenta_senha, name='ferramenta_senha'),
    path('numeros', ferramenta_numeros, name='ferramenta_numeros'),
    path('recibos', ferramenta_recibos, name='ferramenta_recibos'),
]