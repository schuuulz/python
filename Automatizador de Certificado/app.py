####### código inspirado no https://www.youtube.com/watch?v=VwYqakOB4ow&ab_channel=DevAprender%7CJhonatandeSouza #######

# Importando as bibliotecas
import openpyxl
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
# Abrindo a planilha
tabela_alunos = openpyxl.load_workbook('alunos_certificados.xlsx')
pagina_alunos = tabela_alunos['Alunos']

# Para cada linha a partir de uma linha especifica
# iniciando a partir da linha 2 | Para fins de test colocar "max_row=2" que ele vai no maximo ate a linha 2 ou ate o nmr que voce especificar                                                   \/
for indice, linha in enumerate(pagina_alunos.iter_rows(min_row=2)):
    nome_aluno = linha[0].value
    data_inicio = linha[1].value
    data_conclusao = linha[2].value
    papel = linha[3].value
    carga_horaria = linha[4].value
    data_emissao = linha[5].value

    # definindo as fontes
    nome_fonte = ImageFont.truetype('./fonts/Madina.ttf', 166)
    data_fote = ImageFont.truetype('./fonts/Dance.otf', 30)

    # escrevendo os dados da planilha para o certificado

    certificado = Image.open('./certificado.png')
    desenhar = ImageDraw.Draw(certificado)

    desenhar.text((360, 367), nome_aluno, fill='black', font=nome_fonte)
    desenhar.text((362, 658), data_emissao.strftime("%d/%m/%Y"), fill='black', font=data_fote)
    certificado.save(f'./Certificados Assinados/{indice} {nome_aluno}.png')
