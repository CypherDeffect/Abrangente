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

def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
