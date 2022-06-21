tupla=(1,3,4,9,11)
lista=[2,3,4,6,7,8,9]

#la tupla no puede ser modificada
#la lista si puede ser modificada

a = lista[0]
print (a)

lista[5] = 14 #reemplazo el valor 5 de la lista por 14
print(lista)

del lista[1] #borro el elemento 1 de la lista
print (lista)

#la tupla se comporta igual a la hora de traer valores, pero no pueden ser modificadas.

lista.append(3) #agrego el valor 3 a la lista
print(lista)
