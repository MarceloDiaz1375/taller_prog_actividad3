def valor_maximo(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def mayor_dos_numeros(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a
    
    
def mayor_tres_numeros(a, b, c):
    mayor_de_dos = mayor_dos_numeros(a, b)
    if mayor_de_dos:
        if mayor_de_dos > c:
            return mayor_de_dos
        elif mayor_de_dos < c:
            return c
        else:
            return c
    else:
        return mayor_de_dos(a, c)
    
def ingresar_numero():
    try:
        num = float(input("Ingrese un numero: "))
        return num
    except:
        print('Valor no reconocido, se asigno 0')
        return 0


if __name__ == "__main__":

    lista_numeros = []
    
    num1 = ingresar_numero()
    lista_numeros.append(num1)

    num2 = ingresar_numero()
    lista_numeros.append(num2)

    num3 = ingresar_numero()
    lista_numeros.append(num3)

    print(lista_numeros)

    #resultado = mayor_tres_numeros(num1, num2, num3)
    resultado = valor_maximo(lista_numeros)
    
    print(f"El valor máximo entre los tres números ingresados es: {resultado}")