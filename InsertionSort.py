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

list=[10,1,5,0,6,8,7,3,11,4]

i=1
while(i<10):
  element=list[i]
  j=i
  i=i+1

  while(j>0 and list[j-1]>element):
    list[j]=list[j-1]
    j=j-1

  list[j]=element

i=0
while(i<10):
  print (list[i])
  i=i+1