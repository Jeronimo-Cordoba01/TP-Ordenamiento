import time
array = [1,4,3,5,2]
start = time.time() #Medir el tiempo
for i in range(0, len(array)-1): #pivote verde
    for j in range(i +1, len(array)):#pivote naranja
        if array[i] > array[j]: #Menor a mayor
            auxiliar = array[i]
            array[i] = array[j]
            array[j] = auxiliar

for i in range(0, len(array)-1): #pivote verde
    for j in range(i +1, len(array)):#pivote naranja
        if array[i] < array[j]: #Mayor a menor
            auxiliar = array[i]
            array[i] = array[j]
            array[j] = auxiliar

end = time.time() #Detener el tiempo
 
print(array)
