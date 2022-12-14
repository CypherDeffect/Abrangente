!wget https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ultimas-4-semanas-glp.csv/@@download/file/ultimas-4-semanas-glp.csv

import  csv
import copy
import time

listaDePrecos = []
error = []

with open('/content/ultimas-4-semanas-glp.csv', encoding='iso-8859-1') as csv_file:
    csv = csv.reader(csv_file, delimiter=';' )
    next(csv)
    for row in csv:
        valor = float(row[12].replace(',','.'))
        listaDePrecos.append(valor)

print(listaDePrecos)

# Bubble Sort #

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)


