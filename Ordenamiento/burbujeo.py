import time
contador = 0
array = [3,0,1,4,7,2,5,6]
start = time.time() #Medir el tiempo
for i in range(0, len(array)-1): #pivote verde
    for j in range(i +1, len(array)):#pivote naranja
        contador += 1
        print(array)
        if array[i] > array[j]: #Menor a mayor
            auxiliar = array[i]
            array[i] = array[j]
            array[j] = auxiliar

# for i in range(0, len(array)-1): #pivote verde
#     for j in range(i +1, len(array)):#pivote naranja
#         if array[i] < array[j]: #Mayor a menor
#             auxiliar = array[i]
#             array[i] = array[j]
#             array[j] = auxiliar

end = time.time() #Detener el tiempo
print(contador)
