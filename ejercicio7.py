from random import randint

def crear_matriz_random(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = randint(0, 20)
            fila.append(numero)
        matriz.append(fila)
    return matriz

def factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    return factorial

def calcular_suma_diagonal(matriz):
    suma_diagonal = 0
    for i in range(len(matriz)):
        suma_diagonal += matriz[i][i]
    return suma_diagonal

def lista_k(matriz):
    lista_k = []
    suma_diagonal = calcular_suma_diagonal(matriz)
    for lista in matriz:
        for numero in lista:
            factorial_num = factorial(numero)
            if factorial_num >= suma_diagonal:
                lista_k.append(numero)
    
    #print(lista_k)
    lista_sin_repetidos = []
    for numero in lista_k:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)

    return lista_sin_repetidos

if __name__ == "__main__":

    # matriz1 = [
    # [2, 5, 8, 21],
    # [4, 21, 12, 7],
    # [12, 3, 9, 5],
    # [21, 2, 17, 12]
    # ]
    
    # resultado = factorial(5)
    # print(resultado)
    
    # resultado2 = calcular_suma_diagonal(matriz1)
    # print(resultado2)

    # resultado3 = lista_k(matriz1)
    # print(resultado3)
    try:
        while True:
            filas = int(input("Ingrese la cantidad de filas de la matriz: "))
            columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
            if filas == columnas:
                break
            else:
                print("La matriz no es cuadrada")
        resultado = crear_matriz_random(filas, columnas)
        print(f"\nMatriz generada:")
        for lista in resultado:
            print(lista)
        print("\n")
        resultado = lista_k(resultado)
        print(f"Lista K: {resultado}")
        resultado.sort()
        print(f"Lista K ordenada: {resultado}")

    except Exception as e:
        print(f"\nOcurrio un error: {e}")
        print("Solo se aceptan numeros enteros")