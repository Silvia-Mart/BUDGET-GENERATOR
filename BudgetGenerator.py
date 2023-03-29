import PySimpleGUI as sg
import sys
import locale
from fpdf import FPDF

def dados_empresa():
    dic_empresa = {
        "nome_empresa" : "Industrias LifeLong",
        "whatsapp_empresa" : "(11) 1111-1111",
        "email_empresa" : "lifelongindustrias@gmail.com",
        "end_empresa" : "Rua das Flores, 123- Cidade BR"
    }
    return dic_empresa

sg.theme('DarkBlue')
dados = [  [sg.Text('Dados para o Orçamento')],
           [sg.Text()],
           [sg.Text('Digite o nome do cliente: '), sg.InputText(size=(90, 1))],
           [sg.Text('Digite o whatsapp do cliente: '), sg.InputText(size=(90, 1))],
           [sg.Text('Digite o email do cliente: '), sg.InputText(size=(90, 1))],
           [sg.Text()],
           [sg.Text('Digite o nome do projeto: '), sg.InputText(size=(90, 1))],
           [sg.Text('Digite o valor da hora trabalhada: '), sg.InputText(size=(90, 1))],
           [sg.Text('Digite a quantidade de horas estimadas do projeto : '), sg.InputText(size=(90, 1))],
           [sg.Text('Digite o prazo em dias para a entrega do projeto: '), sg.InputText(size=(90, 1))],
           [sg.Text()],
           [sg.Button('Salvar'), sg.Button('Cancelar')] ]

window = sg.Window('Budget Generator', dados, size=(800,500))

def salvar_orcamento():
    dados_projeto_cliente = {
            "nome_cliente" : values[0],
            "whatsapp_cliente" :  values[1],
            "email_cliente" :  values[2],
            "nome_projeto" :  values[3],
            "valor_hora" :  values[4],
            "hora_estimada" : values[5],
            "prazo_estimado" :  values[6]

        }
    nome_cliente = dados_projeto_cliente['nome_cliente']
    whatsapp_cliente = dados_projeto_cliente['whatsapp_cliente']
    email_cliente = dados_projeto_cliente['email_cliente']
    nome_projeto = dados_projeto_cliente['nome_projeto']
    valor_hora = dados_projeto_cliente['valor_hora']
    hora_estimada = dados_projeto_cliente['hora_estimada']
    prazo_estimado = dados_projeto_cliente['prazo_estimado']

    valor_final = float(valor_hora) * int(hora_estimada)

    locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
    valor_final_formatado = locale.currency(valor_final)
    valor_final_formatado = locale.currency(valor_final, grouping=True)

    valor_hora_formatado = locale.currency(float(valor_hora))
    valor_hora_formatado = locale.currency(float(valor_hora), grouping=True)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', 'B', 24)

    pdf.image("template_orçamento_executivo.png", x = 0 , y = 0)
    pdf.image("lifelong_logo_executivo.png", x = 128 , y = 4)

    pdf.set_text_color(210, 185, 116) 
    pdf.text(15, 15, dados_empresa()["nome_empresa"].upper())

    pdf.set_font('Times', 'BI', 14)

    pdf.text(15, 35, dados_empresa()["whatsapp_empresa"])
    pdf.text(15, 45, dados_empresa()["end_empresa"])
    pdf.text(15, 55, dados_empresa()["email_empresa"])

    pdf.set_font('Times', 'BI', 18)

    pdf.set_text_color(0,0,0) 
    pdf.text(43, 82, nome_cliente.title())
    pdf.text(43, 92, email_cliente)
    pdf.text(43, 102, whatsapp_cliente)

    pdf.set_font('Times', 'B', 18)

    pdf.text(57, 137, nome_projeto.title())
    pdf.text(155, 154, valor_hora_formatado)
    pdf.text(155, 170, hora_estimada)
    pdf.text(155, 186, prazo_estimado)

    pdf.set_text_color(255,255,255)  
    pdf.text(155, 208, valor_final_formatado)

    pdf.output(f"ORCAMENTO {nome_projeto.upper()}.pdf")
    print("Orçamento finalizado com sucesso.")
    sg.popup('Orçamento salvo com Sucesso!')
    

def clear_input(window):
    for key, element in window.key_dict.items():
        if isinstance(element, sg.Input):
            element.update(value='')
            
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'Salvar':
        salvar_orcamento()
        clear_input(window)
        
window.close()
