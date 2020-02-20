# Programa de Junção de colunas
# @ngeorg on Twitter
# PortfolioBuild

# Junção de 3 colunas de 3 planilhas.

# importações

import pandas as pd

# Informar a Localização das 3 planilhas
# sheet[n]_location é a localização das planilhas, todas estão na mesma pasta.

sheet1_location = "planilha1.xlsx" # d in function
sheet2_location = "planilha2.xlsx" # e in function
sheet3_location = "planilha3.xlsx" # f in function

# Informar o Nome das 3 Colunas (uma de cada planilha)
# o Valor a ser informado entre as aspas (str) é o nome do cabeçalho da planilha.

coluna1 = "a"
coluna2 = "b"
coluna3 = "c"

# Função de união dos valores

def unite(a=coluna1, b=coluna2, c=coluna3, d=sheet1_location, e=sheet2_location, f=sheet3_location):

# a = Cabeçalho da Planilha1
# b = Cabeçalho da Planilha2
# c = Cabeçalho da Planilha3

# d = Localização da Planilha1
# e = Localização da Planilha2
# f = Localização da Planilha3

    sheet1 = open(d, 'rb')
    s1read= pd.read_excel(sheet1)
    column1 = s1read[coluna1]


    sheet2 = open(e, 'rb')
    s2read= pd.read_excel(sheet2)
    column2 = s2read[coluna2]

    sheet3 = open(f, 'rb')
    s3read= pd.read_excel(sheet3)
    column3 = s3read[coluna3]

    new = pd.DataFrame({"Coluna 1" : column1,
                        "Coluna 2" : column2,
                        "Coluna 3" : column3})

    print(new)

unite()

