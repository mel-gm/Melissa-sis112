suma = 0
promedio = 0
cantidad = int(input("Ingrese la cantidad de estudiantes a evaluar: "))
notas = []

for i in range(cantidad):
    nota = int(input("Ingrese la nota del estudiante: "))
    notas.append(nota)

suma = sum(notas)
promedio = suma / cantidad

print("Las notas son:", notas)
print("La suma de las notas es:", suma)
print("El promedio de las notas es:", promedio)






