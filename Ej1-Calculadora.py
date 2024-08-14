contador = 0
print("--- CALCULADORA ---")
while contador != 6:
    print("1. Suma")
    print("2. Resta")
    print("3. Múltiplicación")
    print("4. División")
    print("5. Salir")
    elegir = int(input("Elija una opción: "))
    if elegir == 1:
        numero1= int(input("Ingrese el primer número a evaluar: "))
        numero2= int(input("Ingrese el segundo número a evaluar: "))
        suma = numero1 + numero2
        print("La suma es: " + str (suma))
    elif elegir == 2:
        numero1= int(input("Ingrese el primer número a evaluar: "))
        numero2= int(input("Ingrese el segundo número a evaluar: "))
        resta = numero1 - numero2
        print("La resta es: "+ str(resta))
    elif elegir == 3:
        numero1= int(input("Ingrese el primer número a evaluar: "))
        numero2= int(input("Ingrese el segundo número a evaluar: "))
        multi= numero1 * numero2
        print("La multiplicación es: "+str(multi))
    elif elegir == 4:
        numero1= int(input("Ingrese el primer número a evaluar: "))
        numero2= int(input("Ingrese el segundo número a evaluar: "))
        divi= numero1/numero2 
        print("La división es: "+str(divi))
    else:
        print("--- Eso es todo :/, Gracias ---")

operacion = input("Elija una operación: ")
def suma (a,b):
    resultado = a+b
    return
def resta (a,b):
    resultado = a-b
    return
def multi (a,b):
    resultado = a*b
    return
def divi (a,b):
    resultado = a/b
    return


    





        






