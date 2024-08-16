
def suma(numero1, numero2):
    return numero1 + numero2
def resta(numero1, numero2):
    return numero1 - numero2
def multiplicacion (numero1, numero2):
    return numero1 * numero2
def division(numero1, numero2):
    if numero2 == 0:
        return ("No existe división entre 0")
    return numero1 / numero2
def calculadora():
    contador = 0
    print ("--- CAlCULADORA ---")
    while contador != 6:
        print("1. Suma")
        print("2. Resta")
        print("3. Múltiplicación")
        print("4. División")
        print("5. Salir")
        elegir = int(input("Elija una opción: "))
        if elegir == 1:
            numero1 = int(input("Ingrese el primer número a evalular: "))
            numero2 = int(input("Ingrese el segundo número a evalular: "))
            resultado = suma(numero1, numero2)
            print("La suma es: " + str(resultado))
        elif elegir == 2:
            numero1 = int(input("Ingrese el primer número a evalular: "))
            numero2 = int(input("Ingrese el segundo número a evalular: "))
            resultado = resta(numero1, numero2)
            print("La resta es: " + str(resultado))
        elif elegir == 3:
            numero1 = int(input("Ingrese el primer número a evalular: "))
            numero2 = int(input("Ingrese el segundo número a evalular: "))
            resultado = multiplicacion(numero1, numero2)
            print("La multiplicación es: " + str(resultado))
        elif elegir == 4:
            numero1 = int(input("Ingrese el primer número a evalular: "))
            numero2 = int(input("Ingrese el segundo número a evalular: "))
            resultado = division(numero1, numero2)
            print("La división es: " + str(resultado))
        elif elegir == 5:
            print ("--- Eso es todo :/, Gracias ---")
            break
        else:
            print(">>> Por favor elija de nuevo <<<")
calculadora ()











        






