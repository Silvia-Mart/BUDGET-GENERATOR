import locale
from fpdf import FPDF

#Dados da Empresa
nome_empresa = input("Nome da empresa: ")
whatsapp_empresa = input("Whatsapp da empresa: ")
email_empresa = input("e-mail da empresa: ")
end_empresa = input("Endereço da empresa: ")

#Dados do Cliente
nome_cliente = input("Nome do Cliente: ")
whatsapp_cliente = input("Whatsapp do cliente: ")
email_cliente = input("e-mail do cliente: ")

#Dados do Orçamento
nome_projeto = input("Nome do projeto: ")
valor_hora = input("Valor da hora trabalhada: ")
hora_estimada = input("Horas estimadas do projeto: ")
prazo_estimado = input("Prazo estimado em dias para entrega: ")

valor_final = float(valor_hora) * int(hora_estimada)

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
valor_final_formatado = locale.currency(valor_final)
valor_final_formatado = locale.currency(valor_final, grouping=True)

valor_hora_formatado = locale.currency(float(valor_hora))
valor_hora_formatado = locale.currency(float(valor_hora), grouping=True)

#adicionando informações no design
pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', 'B', 24)

pdf.image("template_orçamento_executivo.png", x = 0 , y = 0)
pdf.image("lifelong_logo_executivo.png", x = 128 , y = 4)

pdf.set_text_color(210, 185, 116)  
pdf.text(15, 15, nome_empresa)

pdf.set_font('Times', 'BI', 14)

pdf.text(15, 35, whatsapp_empresa)
pdf.text(15, 45, end_empresa)
pdf.text(15, 55, email_empresa)

pdf.set_font('Times', 'BI', 18)

pdf.set_text_color(0,0,0) 
pdf.text(43, 82, nome_cliente)
pdf.text(43, 92, email_cliente)
pdf.text(43, 102, whatsapp_cliente)

pdf.set_font('Times', 'B', 18)

pdf.text(57, 137, nome_projeto)
pdf.text(155, 154, valor_hora_formatado)
pdf.text(155, 170, hora_estimada)
pdf.text(155, 186, prazo_estimado)

pdf.set_text_color(255,255,255)  
pdf.text(155, 208, valor_final_formatado)

pdf.output(f"ORÇAMENTO {nome_projeto}.pdf")
print("Orçamento finalizado com sucesso.")