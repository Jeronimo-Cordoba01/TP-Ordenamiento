c = 0
def swap(a: int, b: int):
    return b,a

def particionar(array, low, high):
    pivote = array[high] #El pivote sera el ultimo elemento de la lista
    i = low - 1
        
    for j in range(low, high):
        
        if array[j] <= pivote:
            i += 1
            array[i], array[j] = swap(array[i], array[j])
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] )
    
    return i + 1
    
def quick_sort(array, low, high):
    global c
    c += 1
    if low < high:
        pi = particionar(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
"""El algoritmo de quick sort mostrado en clase lo que hace es: Con la funcion swap toma dos enteros, y los retorna con los valores intercambiados.
Luego en la funcion particionar tenemos el pivote, que es el ultimo elemento del array,
despues se inicializa el indice i como el menor valor menos 1 (low -1), con el bucle for recorre todos los elementos desde el mas bajo (low) hasta el mas alto (high).
Si un elemento es menor o igual al pivote, se incrementa i y se intercambian los elementos en array[i] y array[j].
 Luego, se intercambia el pivote con el primer elemento mayor encontrado.
La funcion quicksort lo que hace es llamarse de forma recursiva dos veces, una para la subcadena de la izquierda del pivote y otra para la derecha,
 la condicion continua hasta que low es mayor o igual a high"""

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
start = time.time()
quick_sort(vector, 0 , len(vector) - 1)
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")
print(c)
print(len(vector))
print(vector)
