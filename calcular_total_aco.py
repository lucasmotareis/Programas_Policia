import tabula.io as tabula

import pandas as pd
import os

#tabula.read_pdf_with_template("C:/Users/lucas/Downloads/2023/", pages="all")

lista_arquivos = os.listdir('C:/Users/lucas/Downloads/Militares_Lagoa/')
lista_final_militares = []

for pasta_militar in lista_arquivos:

    diretorio = "file:///C:/Users/lucas/Downloads/Militares_Lagoa/"+pasta_militar+'/'
    arquivos_militar = os.listdir('C:/Users/lucas/Downloads/Militares_Lagoa/'+pasta_militar+'/')
    df_final = pd.DataFrame()

    for arquivo in arquivos_militar:
        a = pd.read_excel(diretorio+arquivo)
        df_final = pd.concat([df_final,a])


    df_final_final = df_final[['Unnamed: 3', 'Unnamed: 6']]
    df2 = df_final_final.set_index("Unnamed: 3")
 
    try:
        valor_aco = df2.loc["Ind Escala Extra-Lei 3681/2020", ["Unnamed: 6"]]
        aco_total = 0
        for i in range(len(valor_aco.loc["Ind Escala Extra-Lei 3681/2020"])):
            aco_total += float(str(valor_aco.iloc[i,0]).replace('R$','').replace('.','').replace(',','.'))
        lista_final_militares.append([pasta_militar,aco_total])
    except KeyError:
        print("Valor não encontrado. Ignorando o erro.")


eoq = sorted(lista_final_militares, key=lambda x: x[1])
eoq.reverse()

for i in eoq:
    print(f"{i[0]:50} - R${i[1]:.2f}")
# print(valor_aco.iloc[2,0])
