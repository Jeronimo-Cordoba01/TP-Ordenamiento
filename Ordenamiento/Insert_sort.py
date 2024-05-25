array = [3,0,1,4,7,2,5,6]
contador = 0
for i in range(1, len(array)): #i vale 1 y suma 1 por cada iteracion
    numero_a_comparar = array[i] #nume a comparar vale array en posicion correspondiente por cada iteracion
    pivot = i -1 
    

    while pivot >=  0 and numero_a_comparar < array[pivot]: #mientras que pivot sea mayor o igual a cero y numero a comparar
#(array[i]) sea menor que array en la posicion que indique pivot (i-1) 
#es decir, arranca comparando 0 con 3, y no al reves
        #print(f"{array} 1")
        array[pivot +1] = array[pivot] #array en posicion de pivot +1 va a ser igual al numero que correspondia a array en pivot
        pivot -=1 #Se asegura de comparar con el numero a la izquierda

    array[pivot +1] = numero_a_comparar #asigna el numero desordenado a la derecha
    contador += 1
        
print(array)
print(contador)

        
