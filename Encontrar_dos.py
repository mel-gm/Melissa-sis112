import random
def generarLista(tamañoLista,ValorMinimo,ValorMaximo,lista):
    for i in range(tamañoLista):
        aleatorio=random.randint(ValorMinimo,ValorMaximo)
        lista.append(aleatorio)
    return lista
def encontrarNumero(lista,numero): #busqueda lineal que avanza uno por uno
    for i in range((len(lista))):
        if (numero==lista[i]):
            print(f"numero encontrado en el indice{i}")
            break
        return 1 #si entcontro un valor 
        #else:
            # return -1 #si me retorna un -1 es porque no se a encontrado
    