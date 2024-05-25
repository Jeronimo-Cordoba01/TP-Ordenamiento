"""
Participantes: Jerónimo Córdoba - Valetin Corallo - Lautaro Alderete - Carlos Lopez
---
Clase 9: TP - Ordenamiento
---
Enunciado: 
Trabajo Práctico Ordenamiento

Organización en grupos:
Serán asignados a los dojos 1 a 10 (deberán respetar la asignación que realizamos). En caso de inasistencia, 
avisar para que les asignemos una consigna (deberán realizar el trabajo individualmente).

Consigna: 
Parte 1:
Analizar el algoritmo “Quicksort” dado en clases, indicando paso a paso qué hace el algoritmo. 
¿Se les ocurre alguna forma de implementar el algoritmo sin utilizar recursión? ¿Notan diferencias en cuanto a performance? ¿Cuáles?

Parte 2:
Ver el video de la coreografía que simula el ordenamiento de vectores y tomar nota de los pasos clave observados durante el proceso.
Basándote en la coreografía, formalizar un algoritmo que represente la estrategia utilizada para ordenar los elementos del vector.
Describir detalladamente cada paso del algoritmo, incluyfino las operaciones realizadas en cada etapa.
Realizar un análisis comparativo entre el algoritmo formalizado y otros algoritmos de ordenamiento vistos (por ejemplo, burbuja y selección).
Discutir las ventajas y desventajas del algoritmo propuesto en términos de tiempo de ejecución, número de comparaciones necesarias 
y complejidad en el peor caso. Presentar las conclusiones y reflexiones sobre la efectividad y eficiencia del algoritmo propuesto 
en relación con los objetivos de ordenamiento.

Entrega:
Un repositorio aplicando markdown con: el código, el análisis, ventajas y desventajas. Indicar participantes del grupo. 
El repositorio tiene que ser privado y solo serán colaboradores los integrantes del grupo y los docentes de la cátedra.
"""
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

#end = time.time()
vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
print("Vector original:", vector)
quick_sort_iterativo(vector)
print("Vector ordenado:", vector)

start = time.time()
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")

#Hay una diferencia de tiempo entre esta version y la recursiva, siendo esta mas eficiente