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

# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1



original = copy.copy(listaDePrecos)

start_merge = time.time()

mergeSort(listaDePrecos)

end_merge = time.time()

print (end_merge - start_merge)

print(listaDePrecos)
print(original)