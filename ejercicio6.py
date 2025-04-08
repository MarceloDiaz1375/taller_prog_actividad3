from random import randint

def imprimir_matriz(matriz):
    for lista in matriz:
        print(lista)

def crear_matriz_random(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = randint(-10, 10)
            fila.append(numero)
        matriz.append(fila)
    return matriz

def crear_matriz_lista(filas, columnas, lista):
    matriz = []
    cont = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            #numero = randint(-10, 20)
            fila.append(lista[cont])
            cont += 1
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz1, matriz2):
    matriz_resultante = []
    for lista1, lista2 in zip(matriz1, matriz2):
        lista_resultante = []
        for numero1, numero2 in zip(lista1, lista2):
            lista_resultante.append(numero1+numero2)
        matriz_resultante.append(lista_resultante)
    return matriz_resultante

def columnas_matriz(matriz):
    cont = 0
    columnas = []
    for i in range(len(matriz[0])):
        columna = []
        for lista in matriz:
            #print(matriz[j][i])
            columna.append(lista[i])
        cont += 1
        columnas.append(columna)
    return columnas

def producto_matrices(matriz1, matriz2):
    columnas_matriz2 = columnas_matriz(matriz2)
    lista_resultante = []
    for i in range(len(matriz1)):
        for j in range(len(columnas_matriz2)):
            print(matriz1[i][j] * columnas_matriz2[i][j])

            #lista.append()

    return lista_resultante


if __name__ == "__main__":

    try:
        while True:
            print("*** Suma de matrices ***")
            filas = int(input("Ingrese la cantidad de filas de las matrices: "))
            columnas = int(input("Ingrese la cantidad de columnas de las matrices: "))
            if filas == columnas:
                break
            else:
                print("Las matrices no son cuadradas")
        matriz1 = crear_matriz_random(filas, columnas)
        matriz2 = crear_matriz_random(filas, columnas)
        print(f"\nMatriz 1:")
        imprimir_matriz(matriz1)
        print(f"\nMatriz 2:")
        imprimir_matriz(matriz2)
        print("\n")
        resultado = sumar_matrices(matriz1, matriz2)
        print("Matriz resultante")
        imprimir_matriz(resultado)
    except Exception as e:
        print(f"\nOcurrio un error: {e}")
        print("Solo se aceptan numeros enteros")
