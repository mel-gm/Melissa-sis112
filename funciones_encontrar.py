import Encontrar_dos 
import time
listaNum=[]
listComp=int(input("Ingrese la cantidad de datos para la lista: "))
minAl=int(input("Ingresar cantidad minima para generar los numeros aleatorios: "))
mixAl=int(input("Ingrese el número maximo para generar los numeros aleatorios: "))

inicio=time.time()
Encontrar_dos.generarLista(listComp,minAl,mixAl,listaNum)
fin=time.time()

print(f"Tiempo transcurrido de la generacion de la lista \n {(fin-inicio)*1000}ms")

print(listaNum)
print(len(listaNum))
print(type(listaNum))

numeroaEncontrar=int(input("Ingrese el numero a encontrar: "))
inicio=time.time()
Encontrar_dos.encontrarNumero(listaNum,numeroaEncontrar)
fin=time.time()
print(f"tiempo transcurrido de la generación de la lista \n {(fin-inicio)*1000} ms ")

x=sorted(listaNum)
print(x)

