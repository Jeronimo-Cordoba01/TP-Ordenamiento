import time
#start = time.time() #Medir el tiempo
def particionar(array, low, high):
    pivote = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort_iterativo(array):
    # Inicializar la pila con el rango completo del array
    array_vacio = [(0, len(array) - 1)]
    contador = 0
    

    # Procesar el array mientras no esté vacía
    while array_vacio:
        # Obtener los índices del subarray del tope de la pila
        low, high = array_vacio.pop()

        if low < high:
            # Particionar el array y obtener la posición del pivote
            pi = particionar(array, low, high)

            # Si hay elementos a la izquierda del pivote, agregar esos índices al array
            if pi - 1 > low:
                array_vacio.append((low, pi - 1))

            # Si hay elementos a la derecha del pivote, agregar esos índices al array
            if pi + 1 < high:
                array_vacio.append((pi + 1, high))
            contador +=1
    print(contador)


#end = time.time()
array = [3,0,1,4,7,2,5,6]
print("Vector original:", array)
quick_sort_iterativo(array)
print("Vector ordenado:", array)

start = time.time()
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")

#Hay una diferencia de tiempo entre esta version y la recursiva, siendo esta mas eficiente
