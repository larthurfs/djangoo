from django import forms

class ReciboForm(forms.Form):
    nome_pagador = forms.CharField(label='Nome do Pagador')
    endereco_pagador = forms.CharField(label='Endereço do Pagador')
    cpf_cnpj_pagador = forms.CharField(label='CPF/CNPJ do Pagador')
    nome_receptor = forms.CharField(label='Nome do Receptor')
    cpf_cnpj_receptor = forms.CharField(label='CPF/CNPJ do Receptor')
    descricao_servico = forms.CharField(label='Descrição do Serviço')
    valor = forms.DecimalField(label='Valor')
    cidade = forms.CharField(label='Cidade')
    data_emissao = forms.DateField(label='Data de Emissão')