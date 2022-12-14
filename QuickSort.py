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

def particao(A, esquerda, direita):
    # 1. Seleção do pivô. O pivô será o elemento A[esquerda].
    pivo = A[esquerda]
    # Particionamento do arranjo.
    i = esquerda
    j = direita
    while i <= j:
        # Encontra elemento maior que o pivo.
        while A[i] <= pivo:
            i += 1
            if i == direita:
                break

        # Encontra elemento menor que o pivo.
        while pivo <= A[j]:
            j -= 1
            if j == esquerda:
                break

        # Ponteiros i e j se cruzaram.
        if i >= j:
            break

        # Troca elementos encontrados acima de lugar.
        A[i], A[j] = A[j], A[i]

    # Coloca o pivo no lugar certo.
    pivo, A[j] = A[j], pivo

    # j é o índice em que o pivo agora está.
    return j