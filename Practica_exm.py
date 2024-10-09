def menu():
    print("""SISTEMA DE GESTION DE NOTAS
          1.Agregar nota
          2. Eliminar nota
          3.Modificar nota
          4.Modificar todas las notas
          5.Calcular promedio
          6.Obtener nota máxima y mínima
          7.Salir. Elige una opción:""")
def add_nota(notas):
    a=int(input("Ingrese notas: "))
    notas.append(a)
    return notas
def del_notas(notas):
    ind=len(notas)
    a=int(input("Ingrese un indice que quiera borrar: "))
    notas.pop(a)
    return notas
def mod_nota(notas):
    a=int(input("Ingrese indice a modificar: "))
    b=float(input(f"Ingrese el numero a modificar de la lista {notas[a]}: "))
    notas[a]=b
    return
def mostrar_notas(notas):
    for i in range(len(notas)):
        print(f"Notas{i}:")
def calcular_promedio(notas):
    promedio=sum(notas)/len(notas)
    print("El promedio es: "+str (promedio))
    return promedio
def max_min_notas(notas):
    nota_max= max(notas)
    nota_min=min(notas)
    return nota_max,nota_min
