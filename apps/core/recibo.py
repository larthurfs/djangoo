from reportlab.lib.pagesizes import A5
from reportlab.platypus import Table, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def header(width, height):
    text = "Recibo"
    style = ParagraphStyle(name='HeaderStyle', parent=getSampleStyleSheet()['Heading1'], alignment=1, fontSize=18)
    para = Paragraph(text, style=style)
    res = Table([[para]],width, height)
    res.setStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ])
    return res


def body(width, height, nome_pagador, cpf_cnpj_pagador, descricao_servico, cidade, data_emissao, valor):
    text = f"Recebi(emos) de {nome_pagador}, CPF/CNPJ nº {cpf_cnpj_pagador}, a importância de {valor} reais referente à(ao) Serviço Prestado: {descricao_servico}.\nPara maior clareza, firmo(amos) o presente recibo para que produza os seus efeitos, dando plena, rasa e irrevogável quitação, pelo valor recebido.\n{cidade}, {data_emissao}"

    para = Paragraph(text)
    result = [para]
    widthlist = [width * 5 / 100, width * 90 / 100, width * 5 / 100]
    heightlist = [height * 100 / 100]

    res = Table([
        ["", result, ""]],
        widthlist, heightlist)

    res.setStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])
    return res


def ass(width, height, nome_receptor,cpf_cnpj_receptor):
    widthlist = [width*25/100,width*50/100,width*25/100]
    campoassinatura="______________________________"
    text = [Paragraph(campoassinatura), Paragraph(nome_receptor), Paragraph(cpf_cnpj_receptor)]
    res = Table([["",text,""]],widthlist, height)
    res.setStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ])
    return res


def footer(width, height,endereco_pagador):
    text = endereco_pagador
    res = Table([[text]],width, height)
    res.setStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ])
    return res

def gerador_recibo(pdf, nome_pagador, cpf_cnpj_pagador, descricao_servico, cidade, data_emissao, valor, nome_receptor, cpf_cnpj_receptor, endereco_pagador):

    pdf.setTitle("Recibo")
    width, height = [A5[1], A5[0]]
    heightlist = [height * 20 / 100, height * 57 / 100, height * 20 / 100, height * 3 / 100]
    mainTable = Table([[header(width, heightlist[0])],
                       [body(width, heightlist[1], nome_pagador, cpf_cnpj_pagador, descricao_servico, cidade,
                             data_emissao, valor)],
                       [ass(width, heightlist[2], nome_receptor, cpf_cnpj_receptor)],
                       [footer(width, heightlist[3], endereco_pagador)]], colWidths=width, rowHeights=heightlist)
    mainTable.setStyle([
        ('LEFTPADDING', (0, 0), (0, 2), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ])

    mainTable.wrapOn(pdf, 0, 0)
    mainTable.drawOn(pdf, 0, 0)
    pdf.showPage()
    pdf.save()
