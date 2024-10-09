#funciones 
def suma(a,b):
    c=a+b
    print(c)
    return c
def resta(x,y):
    z=x-y
    print(z)
    return z
def sumalist(q):
    resultado=suma(q)
    print(resultado)
def num_num(lista):
    for i in range(len(lista)):
        print(f"indice= {i} valor= {lista[i]}")
