#PARA ACCEDER A ELEMENTOS DE LA LISTA 
lista = ["Lunes", "Martes", "Miercoles",40,5.67,[1,2,3]]
print (lista[0])
print (lista[0:3])

#PARA SABER LA CANTIDAD DE ELEMENTOS QUE HAY EN LA LISTA
print (len(lista))

#Incertar elementos al final de la lista
lista.append("Yo puedo")
lista.insert(2,"I can") # Para incertar en un lugar específico
print (lista)

lista.extend([7,8,9]) # Agregar una lista a la lista principal
print (lista)

# Sumar dos listas
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista3 = lista1 + lista2
print (lista3)

#Sumar elementos de la lista
lista = [4,1,3]
print(sum(lista))
suma = 0

for elemento in lista: #otro metodo
    suma += elemento
print(suma)

#Buscar un elemento en la lista
lista = [1,2,3,7,7, "Trust yourself"]
print ("Trust yourself" in lista)

#Saber en que indice esta el elemento
print (lista.index(1))

#Si existen velores iguales y quiero saber cuantos hay
print (lista.count(7))
contador= lista.count(7)
print(contador)

#Para eliminar 
lista.pop() #elimina el ultimo elemento
lista.pop(2)
print(lista)
lista.remove(1) #Si no se la posición del elemento pero si el valor que quiero eliminar
lista.clear() #borrar toda la lista
print (lista)

#Dar la vuelta a la lista
lista.reverse()
print (lista)

#Ordenar una lista 
lista = [5,4,1,2,6]
lista.sort() #ordenar elementos de menor al mayor
lista.sort(reverse=True) # se ordenan de mayor a menor
print(lista)

# Recorrer los elementos de una cadena
completo = input("Escribe tu nombre completo: ")
nombre=""
for i in completo:
    nombre= nombre+1
    if i == " ":
        break
print ("Tu primer nombre es: ", nombre)

#Multiplicacion de los elementos en una lista 
mi_lista = [1, 2, 3, 4]
resultado = 1
for num in mi_lista:
    resultado *= num
print(resultado)  # Resultado: 24

#Operaciones con condicionales dentro de una lista 
mi_lista = [1, 2, 3, 4, 5, 6]
suma_pares = sum([num for num in mi_lista if num % 2 == 0])
print(suma_pares)  # Resultado: 12

#RESTAR LOS ELEMENTOS DE UNA LISTA
mi_lista = [10, 2, 3]

# Inicializas el resultado con el primer elemento de la lista
resultado = mi_lista[0]

# Restas los demás elementos
for num in mi_lista[1:]:
    resultado -= num

print(resultado)  # Resultado: 5 (10 - 2 - 3)
#OTRA FORMA 
from functools import reduce

mi_lista = [10, 2, 3]
resultado = reduce(lambda x, y: x - y, mi_lista)
print(resultado)  # Resultado: 5

